# src/transform.py
import pandas as pd

def engineer_features(
    orders: pd.DataFrame,
    order_items: pd.DataFrame,
    order_payments: pd.DataFrame,
) -> pd.DataFrame:

    item_agg = (
        order_items
        .groupby("order_id")
        .agg(
            order_revenue=("price", "sum"),
            item_count=("order_item_id", "count"),
        )
        .reset_index()
    )

    df = orders.merge(item_agg, on="order_id", how="left")

    df["delivery_days"] = (
        df["order_delivered_customer_date"] - df["order_purchase_timestamp"]
    ).dt.days

    df["sla_breach"] = (
        df["order_delivered_customer_date"] > df["order_estimated_delivery_date"]
    ).astype(int)

    df["purchase_month"] = df["order_purchase_timestamp"].dt.to_period("M")

    return df.reset_index(drop=True)