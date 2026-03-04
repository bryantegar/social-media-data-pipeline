import pandas as pd
import psycopg2
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load data hasil scraping
df = pd.read_csv("scraper/news_data.csv")

# Koneksi ke PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="social_media_pipeline",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

# Insert data ke table
for index, row in df.iterrows():

    cur.execute(
        """
        INSERT INTO raw_news_mentions 
        (brand, title, link, published_at, scraped_at)
        VALUES (%s,%s,%s,%s,%s)
        ON CONFLICT (link) DO NOTHING
        """,
        (
            row["brand"],
            row["title"],
            row["link"],
            row["published_at"],
            row["scraped_at"]
        )
    )

conn.commit()

logging.info("Data successfully inserted into PostgreSQL")

cur.close()
conn.close()

print("Data successfully inserted!")