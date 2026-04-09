# src/clean.py
import pandas as pd

TIMESTAMP_COLS = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date",
]

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df[TIMESTAMP_COLS] = df[TIMESTAMP_COLS].apply(pd.to_datetime, errors="coerce")
    df = df[df["order_status"] == "delivered"]
    df = df.dropna(subset=["order_delivered_customer_date"])
    df = df.drop_duplicates()
    return df.reset_index(drop=True)