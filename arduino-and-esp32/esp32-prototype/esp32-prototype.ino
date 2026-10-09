#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include "secrets.h" //credentials

//pins
#define DHTPIN 15
#define DHTTYPE DHT11
#define LED_PIN 2
#define BUZZER_PIN 4

#define TEMP_THRESHOLD 25.0

//API and wifi credentials
const char* ssid = SSID;
const char* password = PASS;
const char* api_url = API_URL; 

DHT dht(DHTPIN, DHTTYPE);

unsigned long previousMillis = 0;
const long readInterval = 15000; //15 seconds interval to prevent API spam

void setup() {
  Serial.begin(9600);
  
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  
  dht.begin();
  
  //start wifi connection
  Serial.print("Connecting to wifi: ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  
  //wait until connected
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println("\n Wifi Connected Successfully!");
  Serial.print("ESP32 IP: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  unsigned long currentMillis = millis();
  
  //check if its time to read the sensor
  if (currentMillis - previousMillis >= readInterval) {
    previousMillis = currentMillis;

    float humidity = dht.readHumidity();
    float temperature = dht.readTemperature();

    //check if any read failed
    if (isnan(humidity) || isnan(temperature)) {
      Serial.println("Failed to read DHT sensor!");
      return;
    }

    //alarm
    if (temperature >= TEMP_THRESHOLD) {
      digitalWrite(LED_PIN, HIGH);
      digitalWrite(BUZZER_PIN, HIGH);
    } else {
      digitalWrite(LED_PIN, LOW);
      digitalWrite(BUZZER_PIN, LOW);
    }

    Serial.print("Temp: ");
    Serial.print(temperature);
    Serial.print(" °C | Hum: ");
    Serial.print(humidity);
    Serial.println(" %");

    //send data to API (HTTP POST)
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(api_url);
      
      //specify content type as JSON
      http.addHeader("Content-Type", "application/json");

      //build JSON payload
      String jsonPayload = "{\"temperature\": " + String(temperature) + ", \"humidity\": " + String(humidity) + "}";
      
      //make the POST request
      int httpResponseCode = http.POST(jsonPayload);
      
      if (httpResponseCode > 0) {
        Serial.print("SUCCESS! API Response Code: ");
        Serial.println(httpResponseCode);
      } else {
        Serial.print("ERROR sending to API: ");
        Serial.println(httpResponseCode);
      }
      
      //close connection
      http.end();
    } else {
      Serial.println("Hey! Wifi disconnected!");
    }
  }
}