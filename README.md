# Arduino Environmental Monitor 🌡️

A real-time IoT environmental monitoring system that collects temperature and humidity data from an Arduino-connected DHT11 sensor, logs it to CSV, detects anomalies, and visualizes trends in an interactive dashboard.

![Dashboard](dashboard.png)
> *Dashboard screenshot — add yours here once you run `dashboard.py`*

---

## Features

- **Real-time data logging** — reads temperature & humidity from Arduino over serial every 2 seconds
- **Automatic anomaly detection** — flags readings more than 2 standard deviations from the mean
- **Interactive dashboard** — visualizes trends and anomalies across time using Matplotlib
- **CSV logging** — all data persisted locally for further analysis

---

## Hardware

| Component | Details |
|-----------|---------|
| Microcontroller | Arduino Uno (Elegoo R3) |
| Sensor | DHT11 Temperature & Humidity Sensor |
| Connection | USB Serial (COM5) |

### Wiring

| DHT11 Pin | Arduino Pin |
|-----------|-------------|
| VCC | 5V |
| GND | GND |
| DATA | Pin 2 |

---

## Project Structure

```
arduino-environmental-monitor/
│
├─ sensor_sketch/
│   ─ sensor_sketch.ino   # Arduino- reads DHT11 and prints to serial
│
├─ logger.py               # Reads serial data from Arduino, logs to CSV
├─ dashboard.py            # Loads CSV, detects anomalies, renders dashboard
├─ dashboard.png           # Auto-generated dashboard screenshot
└─ README.md
```

---



### Prerequisites

- Python 3.x
- Arduino IDE
- Elegoo Uno R3 + DHT11 sensor

### Arduino Libraries
 Uses **DHT sensor library** by Adafruit

### Python dependencies
 Uses 
   **pandas**
   **matplotlib.pyplot**
   **pyserial**


## How Anomaly Detection Works

Each reading is compared against the mean and standard deviation of all collected data. Any reading that deviates by more than **2 standard deviations** is flagged as an anomaly and marked with an `X` on the dashboard.


## Possible Future Improvements

- Add a live-updating dashboard 
- Train an ML model to predict future temperature trends
- Add email/SMS alerts when anomalies are detected

---

## Author

**Vansh Alawat** — First-Year Engineering @ Purdue University  
