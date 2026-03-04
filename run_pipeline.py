import os
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

print("Starting pipeline...")

logging.info("Pipeline started")

print("Running scraper...")
os.system("python scraper/google_news_scraper.py")

logging.info("Scraper finished")

print("Loading data to database...")
os.system("python ingestion/load_to_postgres.py")

logging.info("Data ingestion completed")

print("Running sentiment analysis...")
os.system("python ingestion/sentiment_analysis.py")

print("Updating data mart...")
os.system("python ingestion/update_data_mart.py")

logging.info("Data mart updated")

logging.info("Sentiment analysis completed")

print("Pipeline finished successfully!")

logging.info("Pipeline finished successfully")