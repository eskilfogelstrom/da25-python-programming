import requests
from datetime import datetime
import pandas as pd
import sqlite3

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
conn = sqlite3.connect("data/db")

df.to_sql("temp_measurements", conn, if_exists="append", index=False)
