#include <Arduino.h>
#include <WiFi.h>

String name;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() {
 while (!Serial.available());
 name = Serial.readString();
 Serial.println("First Name : "  + name );
}




/*
#include <Arduino.h>
#include <WiFi.h>

String count_str;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() {
 while (!Serial.available());
 count_str= Serial.readString();
 Serial.println("count Number : " + count_str);
}
*/

