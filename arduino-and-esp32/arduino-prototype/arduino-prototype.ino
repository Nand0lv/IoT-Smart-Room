#include <DHT.h>

//Pins
#define DHTPIN 2         //DHT11 pin
#define DHTTYPE DHT11    //DHT type
#define LED_PIN 3        //led pin
#define BUZZER_PIN 4     //buzzer pin

#define TEMP_THRESHOLD 20.0 //triggers the alarm if temperature exceeds 20ºC

// Initialize the sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);//
  
  //initialize led and buzzer
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  
  //start the dht11 sensor
  dht.begin();
  
  Serial.println("Hello!");
}

void loop() {
  //1 second delay
  delay(1000);

  //read humidity and temperature
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();

  //check if any reads failed
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error: Failed to read from DHT11 sensor! Check the cables.");
    return;
  }

  bool alarmActive = false;
  
  if (temperature >= TEMP_THRESHOLD) {
    alarmActive = true;
    digitalWrite(LED_PIN, HIGH);     //turns on led
    digitalWrite(BUZZER_PIN, HIGH);  //turns on buzzer
  } else {
    alarmActive = false;
    digitalWrite(LED_PIN, LOW);      //turns off led
    digitalWrite(BUZZER_PIN, LOW);   //turns off buzzer
  }

  //print results to the serial monitor
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.print(" °C | Humidity: ");
  Serial.print(humidity);
  Serial.print(" % | Alarm: ");
  Serial.println(alarmActive ? "On" : "Off");
}