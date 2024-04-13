int AnalogPin0 = A0;
unsigned long startMicros;

void setup() 
{
   Serial.begin(9600);
   startMicros = micros();
}

void loop() 
{
   char ReceivedByte = Serial.read();
   float value = 0.0;
   
   if (ReceivedByte == '$')
   {
      //delay(1000);
      startMicros = micros(); // Reset the start time in microseconds
   } 

   unsigned long currentMicros = micros() - startMicros; // Calculate elapsed time in microseconds
   value = analogRead(AnalogPin0);
   Serial.print(currentMicros);
   Serial.print("-");
   Serial.println(value); 
   delayMicroseconds(600);
}
