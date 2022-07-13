#include <Arduino.h>
#include <WiFi.h>

int num;

void setup() {
 Serial.begin(115200);
 Serial.setTimeout(1);
}

void loop() {
 while (!Serial.available());
 num = Serial.readString().toInt();
 Serial.println(num + 1 );
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

