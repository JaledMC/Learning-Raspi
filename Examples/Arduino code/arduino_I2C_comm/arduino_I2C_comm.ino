int LDRPin = A0;
int valor;
     
int min = 0;
int max = 1023;

int led = 8;

void setup () {
      Serial.begin(9600);
      pinMode( led, OUTPUT );
}

void loop () {
      if(Serial.available()) {
            char c = Serial.read();
            if (c=='B') {
                  analogWrite(led, 250);
            } else if (c=='L') {
                  valor = analogRead(LDRPin);
                  valor = map(valor, min, max, 0, 100);
                  Serial.println(valor);
            } else if (c=='P') {
                  Serial.println(analogRead(1));
            }
            while(Serial.available()>0) c = Serial.read();
      }
}
