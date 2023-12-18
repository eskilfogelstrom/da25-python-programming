import requests
from datetime import datetime
import pandas as pd

# Extract
res = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=59.3293&lon=18.0686&appid=8f20807cea52eed92572aea82df038d5")

data = res.json()

# Transform
temp_measurement = {
    "temp": data["main"]["temp"],
    "date": datetime.now()
}

df = pd.DataFrame([temp_measurement])

# Load
try: # Try reading old CSV
    old_df = pd.read_csv("data/temp_measurements.csv")
    print(old_df.head())
    combined_df = pd.concat([old_df, df], ignore_index=True)

    combined_df.to_csv("data/temp_measurements.csv", index=False)
except: # If file doesn't exist just create new one
    df.to_csv("data/temp_measurements.csv", index=False)
