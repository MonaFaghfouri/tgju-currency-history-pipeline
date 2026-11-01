# TGJU Currency History Data Pipeline

A Python data-engineering project for collecting, processing, and reporting historical currency market data from TGJU.

> **Portfolio showcase:** The production scraper and API integration are intentionally private. This repository contains a small, runnable data-cleaning demonstration with synthetic sample data; it does not retrieve live market prices.

## Project scope

The private production implementation is designed for historical data for USD, EUR, AED, TRY, and CNY, with paginated API retrieval, retries and backoff, checkpoint-based recovery, normalization, deduplication, and formatted Excel export.

## Public demo

The public `demo.py` illustrates data type conversion, invalid-record handling, deduplication, and chronological sorting using synthetic records.

```bash
python -m pip install -r requirements.txt
python demo.py
```

## Tech stack

Python, Requests, Pandas, Beautiful Soup, OpenPyXL, REST-style API integration.

## Repository contents

- `demo.py`: limited, runnable demonstration of the cleaning stage
- `requirements.txt`: public demo dependencies
- `sample_output/sample_currency_data.csv`: synthetic example records
- `.gitignore`: excludes checkpoints, environment files, and Excel exports

## Notes

This is an independent educational/portfolio project and is not affiliated with TGJU. Data source: https://www.tgju.org/. No real-time data collection is included in the public demo. Respect the source website's applicable terms and access limits.
