# Détails techniques

Sont listés ici quelques détails techniques qui ne sont pas nécessaires à l'utilisation des codes Python/Arduino présentés sur ce dépôt, mais pourraient être utile si vous souhaitez modifier des fonctions pour les réutiliser dans le cadre d'un projet plus abouti.



- Il est possible de choisir le nombre de chiffres après la virgule que la fonction Arduino `print` envoie sur le port série (voir la documentation de [Serial.print](https://www.arduino.cc/reference/en/language/functions/communication/serial/print/)). Quand on transfère des valeurs de tension, on peut choisir un nombre de chiffres après la virgule cohérent avec la précision maximale de l'Arduino : l'Arduino a une précision de 10 bits sur une gamme de 5V, la plus petite unité de tension qu'il peut mesurer (i.e. son seuil de précision) est donc de $5/2^{10} = 0,0048828125 \, \mathrm{V}$. Il n'est donc pas vraiment nécessaire d'afficher plus que 4 chiffres après la virgule.

- Le taux de transfert (baud rate) doit être adapté au débit de données qui va transiter par le port série. Ici le baud rate a été fixé arbitrairement à $250000$, ce qui correspond environ à 25000 caractères ASCII par seconde, soit 25 caractères par milliseconde, ce qui est suffisant pour transférer deux unsigned long (de max 10 caractères chacun) à 1 kHz.

- La fonction [micros()](https://www.arduino.cc/reference/en/language/functions/time/micros/) est utilisée pour mesurer les timings dans les deux sketchs Arduino. Si l'on n'a pas besoin d'une grande fréquence d'acquisition on peut la remplacer par la fonction [millis()](https://www.arduino.cc/reference/en/language/functions/time/millis/).

- Les deux fonctions Python qui récupèrent les données envoyées sur le port série utilisent implicitement le fait que l'Arduino Uno fait un reset lorsque la connexion port série est démarrée (c'est pour cela que la première ligne de texte récupérée sur le port série est toujours `Debut de l'acquisition` qui est envoyée lors de l'exécution de la fonction `setup` de l'Arduino). Si pour une raison ou pour une autre vous utilisez un modèle d'Arduino qui ne fait pas de reset pas lorsqu'on démarre la connexion via le port série, il est possible qu'il y ait de problèmes de lecture des données transmises (en particulier si le script Python récupère une ligne qui n'est pas complète, il ne pourra pas la déchiffrer correctement et des valeurs aberrantes apparaîtront dans les tableaux de données). En théorie la fonction [portserie.reset_input_buffer()](https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.reset_input_buffer) appelée dans le script Python est censée vider le cache avant qu'on commence à lire ce qui est envoyé sur le port série pour éviter ces problèmes, mais dans certains tests que j'ai faits en essayant de lire "à la volée" des données sur le port série alors que l'Arduino était déjà en fonctionnement (sans lui imposer de faire un reset au début de la mesure) cela ne semblait pas être suffisant pour éviter les erreurs de lecture.

