# src/ingest.py
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW = PROJECT_ROOT / "data" / "raw"

DATASETS: dict[str, str] = {
    "customers":                        "olist_customers_dataset.csv",
    "geolocation":                      "olist_geolocation_dataset.csv",
    "order_items":                      "olist_order_items_dataset.csv",
    "order_payments":                   "olist_order_payments_dataset.csv",
    "order_reviews":                    "olist_order_reviews_dataset.csv",
    "orders":                           "olist_orders_dataset.csv",
    "products":                         "olist_products_dataset.csv",
    "sellers":                          "olist_sellers_dataset.csv",
    "category_translation":             "product_category_name_translation.csv",
}

def load_all() -> dict[str, pd.DataFrame]:
    return {name: pd.read_csv(RAW / filename) for name, filename in DATASETS.items()}

if __name__ == "__main__":
    dfs = load_all()
    for name, df in dfs.items():
        print(f"{name:30s} {df.shape}")