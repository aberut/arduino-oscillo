const int PinMes1 = A0; // pin qui recevra un signal à mesurer
const int PinMes2 = A1; // pin qui recevra un autre signal à mesurer
const unsigned long delais = 10000; // temps (en µs) entre deux points de mesure (fixe la fréquence d'acquisition)

int mes1; // variable qui stockera la valeur mesurée (sur 10 bits) par le capteur 1
int mes2; // variable qui stockera la valeur mesurée (sur 10 bits) par le capteur 2
unsigned long timing = 0; // variable qui stockera l'instant de la dernière mesure
float tension1; // variable qui stockera la valeur de tension reçue sur le capteur 1
float tension2; // variable qui stockera la valeur de tension reçue sur le capteur 2

void setup() {
  Serial.begin(250000);
  Serial.println("Debut de l'acquisition"); // on envoie un message sur le port série pour dire qu'on a démarré l'acquisition
}

void loop() {
  // on déclecnhe la mesure à chaque fois que le temps écoulé depuis la dernière mesure dépasse le délais fixé
  if(micros()-timing>=delais){
    timing = micros();
    mes1 = analogRead(PinMes1);
    mes2 = analogRead(PinMes2);
    
    tension1 = (mes1/1024.0) * 5.0; // on convertit la valeur entre 0 et 1023 en une tension entre 0 et 5 V
    tension2 = (mes2/1024.0) * 5.0; // on convertit la valeur entre 0 et 1023 en une tension entre 0 et 5 V
  
    // on envoie les valeurs mesurée sur le port série
    Serial.print(tension1);
    Serial.print("\t"); // on sépare les mesures par une tabulation
    Serial.println(tension2); // pour la dernière mesure on fait un println pour sauter une ligne
    }
}
