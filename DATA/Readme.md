# Weather Data Engineering Pipeline

## Project Overview

A Python-based ETL pipeline designed to collect, clean, and analyze real-time weather data from five Moroccan cities using the Open-Meteo API.

**Status:** Work in Progress

## Technologies

- Python
- REST API (Open-Meteo)
- CSV
- PostgreSQL (planned)
- SQL (planned)
- Apache Airflow (planned)
- Power BI (planned)
- Git & GitHub

## Cities Covered

Casablanca, Rabat, Marrakech, Fes, and Tangier.

## Current Features

- Extract current weather data from a public REST API.
- Collect temperature, humidity, and wind speed.
- Clean and validate weather records.
- Remove duplicate observations.
- Export raw and cleaned datasets to CSV.

## Project Structure

```text
Weather_Data_Engineering/
├── data/
│   ├── weather_raw.csv
│   └── weather_clean.csv
├── extract_weather.py
├── transform_weather.py
└── README.md
```

## How to Run

No additional Python packages are required for the current extraction and transformation scripts.

```bash
python extract_weather.py
python transform_weather.py
```

## Upcoming Improvements

- Load weather observations into PostgreSQL.
- Create analytical SQL queries.
- Automate the ETL pipeline.
- Build an interactive Power BI dashboard.

## Data Source

[Open-Meteo Weather API](https://open-meteo.com/)

This project is being developed as part of a personal Data Engineering portfolio.