int sensor = A0;
int LED = 3;
int botao = 2;
int pressionado;
int luz;
void setup() {
  Serial.begin(9600);
  pinMode(sensor, INPUT);
  pinMode(LED, OUTPUT);
  pinMode(botao, INPUT);
}

void loop() {
  luz = analogRead(sensor);
  pressionado = digitalRead(botao);
  if (pressionado == 1){
    digitalWrite(LED, HIGH);
    delay(3000);
    digitalWrite(LED, LOW);}
    else{
      if(luz<300){
        digitalWrite(LED, HIGH);}
        else{digitalWrite(LED, LOW);
      }
    }
}