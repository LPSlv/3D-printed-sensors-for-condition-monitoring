const int analog_pin = A0;
const unsigned long sampling_interval = 50;
int sensor_value = 0;

void setup() {
  analogReference(DEFAULT);
  Serial.begin(115200);
}

void loop() {
  static unsigned long last_sample_time = 0;
  unsigned long current_time = micros();

  // Pārbauda vai ir pagājis mērījumu intervāls
  if (current_time - last_sample_time >= sampling_interval) {
    sensor_value = analogRead(analog_pin);
    
    // Vērtības nosūtīšana 2 baitos
    Serial.write((uint8_t*)&sensor_value, 2);

    last_sample_time = current_time;
  }
}
