import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np

# Load data
df = pd.read_csv("sensor_data.csv")
df = df[df["timestamp"] != "timestamp"]
df["timestamp"] = pd.to_datetime(df["timestamp"])
df["temperature_c"] = pd.to_numeric(df["temperature_c"])
df["humidity"] = pd.to_numeric(df["humidity"])

# Drop warmup period
df = df[df["timestamp"] > df["timestamp"].min() + pd.Timedelta(minutes=5)]
df = df.reset_index(drop=True)

# use last 5 readings to predict next one
WINDOW = 5
X, y = [], []
for i in range(WINDOW, len(df)):
    X.append(df["temperature_c"].iloc[i-WINDOW:i].values)
    y.append(df["temperature_c"].iloc[i])

X, y = np.array(X), np.array(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae:.4f}°C")

# Plot predicted vs actual
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(y_test)), y_test, label="Actual", color="purple")
ax.plot(range(len(y_pred)), y_pred, label="Predicted", color="orange", linestyle="--")
ax.set_title("Temperature Prediction — Actual vs Predicted")
ax.set_xlabel("Reading #")
ax.set_ylabel("Temperature (°C)")
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("prediction.png", dpi=150, bbox_inches="tight")
plt.show()

print("Prediction complete")