# Utiliser un Arduino et Python pour faire un oscilloscope (basique) :

Vous trouverez ici des exemples de codes Python (sous forme de scripts et de notebooks Jupyter) et de sketch Arduino qui permettent d'utiliser un Arduino Uno comme un oscilloscope basique.

## Pré-requis

Cette page n'est pas un tutoriel détaillé et fait l'hypothèse que vous connaissez au moins les rudiments du fonctionnement d'un Arduino (voir par exemple [Aduino.cc](https://www.arduino.cc/en/Guide)) et que vous avez déjà installé un moyen de lire un code Python (utiliser par exemple [Anaconda](https://www.anaconda.com/products/individual)).

Les fonctions Python présentées requièrent toutes l'utilisation de la library [pyserial](https://github.com/pyserial/pyserial) qui s'installe facilement avec pip ou conda (si vous utilisez Anaconda, ouvrez l'Anaconda Prompt et tapez ``conda install pyserial`` dans l'invite de commande).

## Présentation des fonctions :

Les exemples présentés ici reposent tous sur le même principe général de fonctionnement :

- Un Arduino Uno est configuré pour envoyer des données sur un port série à une fréquence donnée

- Un script Python se charge de récupérer ces données au fur et à mesure de leur arrivée pour pouvoir les exploiter

Il est ainsi possible de :

#### Visualiser en temps réel d'un signal :

Si l'on souhaite simplement visualiser un ou plusieurs signaux en temps réel (comme dans le mode "graph déroulant" d'un oscilloscope), se reporter à la page : [Oscillo-Arduino](./Tuto_oscillo.md)

Une vidéo de démonstration est disponible [ici](./images/demo_notebook.mp4).

#### Acquérir de données avec time-stamp :

Si l'on souhaite plutôt faire une acquisition de donnée, où chaque point de mesure est associé à un "time-stamp" qui indique à quel instant ce point a été mesuré, se reporter à la page : [Mesure-Arduino](./Tuto_mesure.md)

## Dépendances

- [numpy](https://numpy.org/) (tested with ver 1.19.1)
- [matplotlib](https://matplotlib.org/index.html) (tested with ver 3.3.1)
- [pyserial](https://shapely.readthedocs.io/en/latest/manual.html) (tested with ver 3.5)

## License

[MIT](https://choosealicense.com/licenses/mit/) 

(Vous avez le droit illimité d'utiliser, copier, modifier, fusionner, publier, distribuer, vendre et « sous-licencier » l'intégralité de ces codes. Votre seule obligation est d'incorporer la notice de licence et de copyright dans toutes les copies.)
