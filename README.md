# Social Media Monitoring Data Pipeline

This project builds an end-to-end data pipeline that monitors brand mentions from Google News and performs sentiment analysis.

## Features

- Google News scraping using RSS
- Python ETL pipeline
- PostgreSQL data warehouse
- Sentiment analysis using VADER
- Incremental loading (no duplicate data)
- Logging pipeline
- Analytics data mart

## Pipeline Flow

Google News RSS  
↓  
Python Scraper  
↓  
PostgreSQL Raw Table  
↓  
Data Warehouse  
↓  
Sentiment Analysis  
↓  
Analytics Data Mart

## Tech Stack

- Python
- PostgreSQL
- Pandas
- VADER Sentiment
- Apache Airflow (DAG prepared)