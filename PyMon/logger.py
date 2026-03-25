import serial
import csv
from datetime import datetime

PORT = 'COM5'
BAUD = 9600
LOG_FILE = 'sensor_data.csv'

ser = serial.Serial(PORT, BAUD, timeout=2)
print(f"Connected to {PORT}. Ctrl+C to stop")
with open(LOG_FILE, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "temperature_c", "humidity"])

    while True:
        line = ser.readline().decode("utf-8").strip()
        if "Temperature:" in line and "Humidity:" in line:
            try:
                parts = line.split("\t")
                humidity = float(parts[0].replace("Humidity:", "").replace("%", "").strip())
                temp = float(parts[1].replace("Temperature:", "").replace("C", "").strip())
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([timestamp, temp, humidity])
                f.flush()
                print(f"{timestamp} | Temp: {temp}°C | Humidity: {humidity}%")
            except:
                pass
