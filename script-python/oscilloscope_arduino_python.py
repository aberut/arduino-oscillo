# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 13:24:07 2021

@author: Antoine Bérut
"""

import numpy as np
import matplotlib.pyplot as plt
import time
import serial #non installé par défaut dans Anaconda, s'installe avec la commande "conda install pyserial" ou "pip install pyserial"

#%% Réglage des paramètres (vous pouvez modifier cette partie pour l'adapter à vos besoin) :

ser = serial.Serial('COM3', 9600, timeout=None) #on définit le port sur lequel l'arduino est branché

nb_donnees=2 #nombre de valeurs que l'arduino renvoie sur chaque ligne (pour cet exemple : deux tensions entre 0 et 5V)

taille_bloc=10  #nombre de points de mesures dans un "bloc" de données (le programme trace les données bloc par bloc)
nb_bloc_affich=100 #nombre de "blocs" de données qu'on trace sur un même graph (fixe la taille du graph roulant)

nb_bloc_max=10000 #nombre maximal de "blocs" de données qu'on va mesurer (fixe la durée max pendant laquelle on fait des mesures)

y_min=0 #on fixe la valeur minimale de l'axe y
y_max=5 #on fixe la valeur maximale de l'axe y

time.sleep(1) #pause de 1 s pour laisser le temps à l'arduino de démarrer

#%% Vous n'avez normalement pas besoin de modifier en dessous de cette ligne

taille_graph=taille_bloc*nb_bloc_affich #on calcule le nombre de points de données max qui sera affiché sur le graph
data=np.zeros((taille_bloc,nb_donnees)) #on crée un tableau de données de la bonne dimension pour stocker les blocs de données (pour l'instant rempli de zéros)
data_plot=np.zeros((taille_graph,nb_donnees)) #on crée un tableau vide de la bonne dimension pour tracer les données (pour l'instant rempli de zéros)

ser.reset_input_buffer() #élimine tout ce qui peut avoir été envoyé sur le port série avant de commencer les mesures

try :
    print(ser.readline()) #on affiche la première ligne de données envoyée par l'arduino pour vérifier que tout va bien
except:
    print('Problème de réception des données')

#On crée une figure vide (avec la bonne dimension)
fig = plt.figure()
ax = fig.add_subplot(111)
lines =[[] for i in range(nb_donnees)]
for i_donnee in range(nb_donnees):
    lines[i_donnee], = ax.plot(data_plot[:,i_donnee]) #chaque élément de lines stockera le tracé de chacune des entrées de l'oscilloscope
scannline, = ax.plot([0,0],[y_min,y_max],'r--') #la scannline servira à repérer quel est le dernier point de mesure à l'instant t sur le graph déroulant
ax.set_ylim(y_min,y_max)
ax.grid()

t0=time.time()#on mesure l'heure avant de commencer à acquérir les données

#La mesure peut être intérrompue en appuyant sur ctrl + C s'il y a un problème (par exemple si on se rend compte que ça prend beaucoup plus de temps que prévu)
for i_bloc in range(nb_bloc_max) :
    try:
        for i_mes in range(taille_bloc): 
            data_byte = ser.readline() #on récupère les données envoyées ligne par ligne
            data_string = data_byte.decode('ascii') #on transforme les données en chaîne de caractère
            data[i_mes,0:(nb_donnees+1)] = np.fromstring(data_string, dtype=float, sep="\t") #on remplit progressivement le tableau "data" avec les données reçues
        
        #on remplit le tableau "data_plot" avec le dernier bloc de données (en le mettant à la suite du précédent et en bouclant sur le 1er si on dépasse le nombre de bloc maximal)
        indice_debut = (i_bloc % nb_bloc_affich) * taille_bloc #on
        indice_fin = indice_debut+taille_bloc
        data_plot[indice_debut:indice_fin,:] = data
        
        t1=time.time()-t0#on mesure le temps écoulé depuis le début de l'acquisition des données
        
        #on trace les données qui correspondent aux X derniers blocs reçus
        for i_donnee in range(nb_donnees):
            lines[i_donnee].set_ydata(data_plot[:,i_donnee])
        scannline.set_xdata([indice_fin,indice_fin])
        plt.title('Temps écoulé : {:.4} s'.format(t1))
        plt.pause(0.01)
                
    except KeyboardInterrupt:
        print("Vous avez interrompu la lecture") #ce qui s'affiche si on arrête la boucle en appuyant sur ctrl + C
        time.sleep(0.1)
        break

ser.close() #on arrête la connexion avec l'arduino via le port série