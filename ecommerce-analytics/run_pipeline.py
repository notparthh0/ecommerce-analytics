# run_pipeline.py
from pathlib import Path
import pandas as pd

from src.ingest import load_all
from src.clean import clean_orders
from src.transform import engineer_features

PROJECT_ROOT = Path(__file__).resolve().parent
PROCESSED = PROJECT_ROOT / "data" / "processed"

if __name__ == "__main__":
    PROCESSED.mkdir(parents=True, exist_ok=True)

    raw = load_all()
    orders = clean_orders(raw["orders"])
    fact = engineer_features(orders, raw["order_items"], raw["order_payments"])

    out = PROCESSED / "fact_orders.csv"
    fact.to_csv(out, index=False)
    print(f"Saved {len(fact):,} rows → {out}")