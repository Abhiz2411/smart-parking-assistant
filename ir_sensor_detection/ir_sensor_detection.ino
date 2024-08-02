const int NUM_SENSORS = 10;
const int IR_SENSORS[NUM_SENSORS] = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11};

void setup() {
  Serial.begin(9600);
  for (int i = 0; i < NUM_SENSORS; i++) {
    pinMode(IR_SENSORS[i], INPUT);
  }
}

void loop() {
  String status = "";
  for (int i = 0; i < NUM_SENSORS; i++) {
    int sensor_status = digitalRead(IR_SENSORS[i]);
    status += String(sensor_status);
    if (i < NUM_SENSORS - 1) {
      status += ",";
    }
  }
  Serial.println("Combined status: " + status);

  delay(500); // Adjust delay as needed
}