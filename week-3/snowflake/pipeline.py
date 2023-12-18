import snowflake.connector
import pandas as pd
from snowflake.connector.pandas_tools import write_pandas

# Extract
df = pd.read_csv("imdb_top_1000.csv")

# Transform
df["Gross"] = df["Gross"].str.replace(",", "")
df["Gross"] = pd.to_numeric(df["Gross"])
df["Runtime"] = pd.to_numeric(df["Runtime"].str[:-4])

# Load
conn = snowflake.connector.connect(
    user="",
    password="",
    account="",
    database="",
    schema=""
)

write_pandas(conn, df, "movies", auto_create_table=True)
