const int analogPin = A0;
const unsigned long samplingInterval = 50;  // Sampling interval in microseconds (will result in ~160ms)
int sensorValue = 0;

void setup() {
  analogReference(DEFAULT);
  Serial.begin(115200);
}

void loop() {
  static unsigned long lastSampleTime = 0;
  unsigned long currentTime = micros();

  if (currentTime - lastSampleTime >= samplingInterval) {
    sensorValue = (analogRead(analogPin));
    
    // Send sensor value as 2 bytes
    Serial.write((uint8_t*)&sensorValue, 2);

    lastSampleTime = currentTime;
  }
}
