void setup()
{ 
  Serial.begin(115200); 
}

void loop()
{ 
  for (int x = 0; x <100 ; x++)
  {  
    Serial.print("Lectura arduino ");
    Serial.print(x); 
    Serial.print(" : ");
    Serial.println(analogRead(A0));
    delay(300);
  }
}

