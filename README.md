# 🩸 Crimson Ledger

![Version](https://img.shields.io/badge/Version-v0.8.1-crimson)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116-green)
![Status](https://img.shields.io/badge/Status-Active-success)

A market intelligence platform for the Torn Item Market, focused on blood bag trading.

Crimson Ledger analyzes the live market, stores historical data, and provides tools to identify buying opportunities through price tracking, supply analysis, and historical trends.

---

## Features

### Current

- Live Torn API integration
- Supports all blood bag types
- Automatic market pagination
- Market cleaning to remove unrealistic listings
- Market analysis
    - Lowest price
    - Highest price
    - Weighted average
    - Top 5 average
    - Top 10 average
- Bulk purchase calculations
    - Buy 100
    - Buy 500
    - Buy 1000
- SQLite database
- Manual market scanner
- REST API built with FastAPI

---

## Blood Bags Supported

| Blood Type | Item ID |
|------------|--------:|
| A+ | 732 |
| A- | 733 |
| B+ | 734 |
| B- | 735 |
| AB+ | 736 |
| AB- | 737 |
| O+ | 738 |
| O- | 739 |
| Irradiated | 1012 |

---

## Project Structure

```text
CrimsonLedger/

├── app/
│   ├── config/
│   ├── database/
│   ├── routes/
│   └── services/
│
├── data/
│
├── tests/
│
├── .env
├── main.py
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Remioactive/Crimson-Ledger.git
```

Open the project:

```bash
cd Crimson-Ledger
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root.

Example:

```env
TORN_API_KEY=YOUR_API_KEY
```

---

## Running the API

```bash
python -m uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### Home

```
GET /
```

Returns project status.

---

### Market Summary

```
GET /market
```

Returns a summary of every tracked blood bag.

---

### Individual Market

```
GET /market/o-plus
```

Returns a detailed analysis for a specific blood bag.

---

### Manual Scanner

```
GET /scan
```

Runs a complete scan and stores snapshots in the database.

---

## Roadmap

### Completed

- FastAPI backend
- Torn API integration
- Market Analyzer
- Market Cleaner
- SQLite database
- Scanner service
- GitHub integration

### Planned

- Scan history
- Historical API
- Web dashboard
- Discord bot
- Charts
- Buy score
- Opportunity detection

---

## Technologies

- Python
- FastAPI
- SQLite
- Requests
- Git
- GitHub

---

## License

This project is currently under development.
