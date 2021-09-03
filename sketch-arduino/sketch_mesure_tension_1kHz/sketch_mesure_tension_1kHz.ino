const int PinMesTemp = A0; //pin qui recevra le signal du capteur de température
const unsigned long delais = 1000; //valeur (en µs) entre deux points de mesures (fixe la fréquence d'acquisition)

unsigned long timing = 0; //variable qui stockera le dernier instant auquel une mesure a été faite

void setup(){
  Serial.begin(250000);
  Serial.println("Debut de l'acquisition"); //on envoie un message de début sur le port série
}

void loop(){
  //on fait une mesure à chaque fois que le temps écoulé depuis la dernière mesure dépasse le délais fixé
  if(micros()-timing >= delais){
    timing = micros();
    Serial.print(timing);//on envoie sur le port série l'instant de prise de mesure (valeur en µs)
    Serial.print("\t");
    Serial.println(analogRead(PinMesTemp));//on envoie sur le port série la valeur mesurée (en bits) sur la pin choisie
    }
}
