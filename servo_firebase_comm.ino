#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>
#include <Servo.h>

Servo myservo; 

#define FIREBASE_HOST "surveillance-d050d-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "prdWW3zpznywCYHi7w7qLbWeE7I36kH4ZGdjr3uu"
#define WIFI_SSID "digieye"
#define WIFI_PASSWORD "123456789"

void setup() {
  Serial.begin(9600);

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("connecting");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println();
  Serial.print("connected: ");
  Serial.println(WiFi.localIP());
  
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);
 myservo.attach(2); 
 myservo.write(0);
}

void loop() {
  
  int n = Firebase.getInt("motor");
  delay(1000);
  if( n == 1){   
    myservo.write(180);
  }
  if (n == 0 ){
   myservo.write(0);
    }
 }
