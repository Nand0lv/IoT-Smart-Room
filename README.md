# IoT Smart Room

This is an end-to-end Internet of Things (IoT) project which uses ESP32 board to measure temperature and humidity of a room, triggers an alarm locally when temperature is above a specific threshold, and then sends the data to a Python FastAPI backend using HTTP POST requests.

## Features

* **Real-time Monitoring:** Temp/Hum reading with DHT11 sensor every 15 seconds.
* **Local Alarm System:** Activates a LED and an Buzzer if the temperature reaches 25°C or higher.
* **Cloud/Local Logging:** Sends sensor data via Wi-Fi to a local FastAPI server.
* **Data Storage:** Stores all historical readings in a local SQLite database.

## Hardware Requirements

* 1x ESP32 Development Board
* 1x DHT11 Temperature & Humidity Sensor
* 1x Red LED
* 1x 1kΩ resistor
* 1x Active Buzzer
* 1x Breadboard & Jumper Wires

### Wiring Guide

| Component | ESP32 Pin |
| :--- | :--- |
| **DHT11 (Data)** | `D15` |
| **LED (Anode)** | `D2` |
| **Buzzer (Positive)**| `D4` |
| **Power (VCC)** | `3V3` |
| **Ground (GND)** | `GND` |

## Software & Libraries

**For the Microcontroller (Arduino IDE):**
* ESP32 Board Package by Espressif
* `DHT sensor library` by Adafruit
* `WiFi.h` and `HTTPClient.h`

**For the Backend (Python 3.x):**
* `fastapi`
* `uvicorn`
* `sqlalchemy`

## API Endpoints

* `GET /ping` - Network test endpoint to verify connection.
* `POST /data` - Endpoint used by the ESP32 to send JSON payloads like `{"temperature": 24.5, "humidity": 51.2}`.
* `GET /data` - Retrieves all stored historical data from the SQLite database.

## Future Enhancements

* **Web Dashboard:** Build a web interface to visualize historical temperature and humidity data.
* **Hardware Expansion:** Integrate additional sensors for more comprehensive room monitoring.