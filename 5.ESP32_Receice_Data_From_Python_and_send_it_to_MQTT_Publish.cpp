/*
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
 Serial.println("First Name : " + x);
 Serial.println("Last Name : Sanit");
 Serial.println("My Company : Sanmina");
}

*/

#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

const char* ssid = "MyOppoA95";
const char* password = "12340pp04321";

const char* broker = "192.168.55.185";
const char* brokerUser = "myUbuntu";
const char* brokerPass = "yut5678";

const char* outTopic = "esp32_pub/number";


WiFiClient espClient;
PubSubClient client(espClient);
long currentTime, lastTime;
char messages[50];

String nickName;
int number;

unsigned long previous_time = 0;
unsigned long delays = 20000;

void initWiFi() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WIFI network");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print('.');
    delay(1000);
  }
  Serial.println(WiFi.localIP());
}




void reconnect(){
  while(!client.connected()){
    Serial.print("\nConnecting to : ");
    Serial.println(broker);
    
    // ? MQTT Client Name : esp32_pub
    if(client.connect("esp32_pub",brokerUser, brokerPass)){
      Serial.print("\nConnected to : ");
      Serial.println(broker);
    } else{
      Serial.println("\nTrying connect again");
      delay(5000);
    }
  }
}




void setup() {
  Serial.begin(115200);
  Serial.setTimeout(1);
  initWiFi();
  client.setServer(broker, 1883);
}




void loop() {

  
  unsigned long current_time = millis();
  if ((WiFi.status() != WL_CONNECTED) && (current_time - previous_time >= delays)) {
    Serial.print(millis());
    Serial.println("Reconnecting to WIFI network");
    WiFi.disconnect();
    WiFi.reconnect();
    previous_time = current_time;
  }

  if(!client.connected()){
    reconnect();
  }

  client.loop();

  while (!Serial.available()){
    nickName = Serial.readString();
    if(nickName == "chai"){
      Serial.println(nickName);
      sniprintf(messages, 75, "nick name = %s, first name = %s", nickName, "yuttana");
      Serial.print("Sending messages: ");
      Serial.println(messages);
      client.publish(outTopic, messages);
    }
  }


  
  /*
  while (!Serial.available()){
    number = Serial.readString().toInt();
    if(number == 5){
      Serial.println(number);
      sniprintf(messages, 75, "number : %ld", number);
      Serial.print("Sending messages: ");
      Serial.println(messages);
      client.publish(outTopic, messages);
    }
  }
  */

 
  

  /*
  while (!Serial.available()){
    myName = Serial.readString();
    if(myName == "chai"){
      Serial.println("yuttana");
    }
  }
  */
  
  /*
  while (!Serial.available());
  myName = Serial.readString();
  Serial.println("First Name : " + myName);
  Serial.println("Last Name : Sanit");
  Serial.println("My Company : Sanmina");
  */

}









