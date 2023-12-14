import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("sources/invoices.csv")

# Transform
df["total"] = df["total"].str.replace(",", ".")
df["total"] = pd.to_numeric(df["total"])

# Load
df.to_csv("dwh/fact_invoices.csv")