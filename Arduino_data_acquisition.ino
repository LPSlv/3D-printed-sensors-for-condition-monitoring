const int analogPin = A0;
const unsigned long samplingInterval = 199;  // Sampling interval in microseconds

void setup() {
  Serial.begin(115200);  // Set baud rate to 115200
}

void loop() {
  static unsigned long lastSampleTime = 0;
  unsigned long currentTime = micros();

  // Check if it's time to take a new sample
  if (currentTime - lastSampleTime >= samplingInterval) {
    // Read analog value from A0
    int sensorValue = analogRead(analogPin);
    
    // Send current time as raw binary data
    Serial.write((uint8_t*)&currentTime, 4);  // Sending 4 bytes
    
    // Send analog value as raw binary data
    Serial.write((uint8_t*)&sensorValue, 2);  // Sending 2 bytes

    // Update last sample time
    lastSampleTime = currentTime;
  }
}
