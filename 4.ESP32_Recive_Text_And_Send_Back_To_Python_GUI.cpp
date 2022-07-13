
#include <Arduino.h>
#include <WiFi.h>

String x;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() {
 while (!Serial.available());
 x = Serial.readString();
 Serial.println("name : " + x);
}






