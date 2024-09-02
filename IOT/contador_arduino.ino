int contagem = 1;
bool indo = true;
void setup() {
Serial.begin(9600);
Serial.println("Iniciando...");
}

void loop() {
while (contagem <= 10){
  Serial.println(contagem);
  contagem += 2;
  delay(500);
}
contagem -= 4;
while (contagem > 0){
  Serial.println(contagem);
  contagem -= 2;
  delay(500);
  }
if (contagem == 0){
  Serial.println(contagem);
  delay(500);
    contagem = 1;
  }
if (contagem < 0){
    contagem = 0;
  }

}
