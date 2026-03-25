import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sensor_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Anomaly detection
df["temp_anomaly"] = (df["temperature_c"] - df["temperature_c"].mean()).abs() > 2 * df["temperature_c"].std()
df["hum_anomaly"] = (df["humidity"] - df["humidity"].mean()).abs() > 2 * df["humidity"].std()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6), sharex=True)
fig.suptitle("Environmental Monitor Dashboard", fontsize=14, fontweight="bold")

# Temperature
ax1.plot(df["timestamp"], df["temperature_c"], color="purple", label="Temperature")
ax1.scatter(df[df["temp_anomaly"]]["timestamp"],
            df[df["temp_anomaly"]]["temperature_c"],
            color="red", marker="x", s=100, label="Anomaly", zorder=5)
ax1.set_title("Temperature vs Time")
ax1.set_ylabel("Temperature (°C)")
ax1.legend()
ax1.grid(True, alpha=0.3)

# Humidity
ax2.plot(df["timestamp"], df["humidity"], color="magenta", label="Humidity")
ax2.scatter(df[df["hum_anomaly"]]["timestamp"],
            df[df["hum_anomaly"]]["humidity"],
            color="blue", marker="x", s=100, label="Anomaly", zorder=5)
ax2.set_title("Humidity vs Time")
ax2.set_ylabel("Humidity (%)")
ax2.set_xlabel("Time")
ax2.legend()
ax2.grid(True, alpha=0.3)

# Format x-axis timestamps so they don't overlap
ax2.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
fig.autofmt_xdate()

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150, bbox_inches="tight")  # saves for GitHub
plt.show()