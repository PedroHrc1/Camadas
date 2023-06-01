const int periodo = 2000;
const int period1 = F_CPU/9600;

 void myDelay(int tempo) {
  for(int i=0; i<tempo; i++){
    asm("nop");
  }
}




void setup() {
  pinMode(5, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  digitalWrite(5, HIGH);
   delay(2000);
  char byte_enviar = 'A' ;// Byte a ser enviado
  char mascara = 1;
  digitalWrite(5, LOW);
  myDelay(periodo);

  // Envia cada bit do byte pela porta serial
  for(int i=0; i<8; i++){
    digitalWrite(5, byte_enviar >> i & mascara); // Seta o pino 2 como HIGH
      myDelay(periodo);  
    }
  digitalWrite(5, HIGH);
  
  Serial.println(periodo);
  
  
  // digitalWrite(2, HIGH); // Seta o pino 2 como HIGH (stop bit)
  // // Serial.println("HIGH");
  // asm("nop"); 
  // asm("nop"); 
  // asm("nop"); 
  // digitalWrite(2, LOW); // Seta o pino 2 como LOW (início do próximo byte)
  // // Serial.println("LOW");
  // asm("nop"); 
 
  
}

