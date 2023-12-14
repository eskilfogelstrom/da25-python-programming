import pandas as pd
import sqlite3

# Extract
df = pd.read_csv("sources/invoices.csv", index_col="id", parse_dates=["date"])

# Transform
df["total"] = df["total"].str.replace(",", ".")
df["total"] = pd.to_numeric(df["total"])

# Load
con = sqlite3.connect("dwh/db")

df.to_sql("fact_invoices", con, if_exists="replace")

cu_df = pd.read_csv("sources/customers.csv", index_col="id")

cu_df.to_sql("dim_customer", con, if_exists="replace")