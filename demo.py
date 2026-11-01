"""Public demonstration of currency-history data cleaning.

This demo uses synthetic records; the production API client is private.
"""
import pandas as pd


def prepare_sample(records):
    frame = pd.DataFrame(records)
    frame["date"] = pd.to_datetime(frame["date"], errors="coerce")
    frame["close"] = pd.to_numeric(frame["close"], errors="coerce")
    frame = frame.dropna(subset=["date", "close"])
    frame = frame.drop_duplicates(subset=["currency", "date"])
    return frame.sort_values("date", ascending=False).reset_index(drop=True)


if __name__ == "__main__":
    sample = [
        {"currency": "USD", "date": "2026-01-01", "close": 100},
        {"currency": "EUR", "date": "2026-01-01", "close": 120},
        {"currency": "USD", "date": "2026-01-01", "close": 100},
    ]
    print(prepare_sample(sample).to_string(index=False))
