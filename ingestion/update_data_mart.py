import psycopg2
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

conn = psycopg2.connect(
    host="localhost",
    database="social_media_pipeline",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("""
DROP TABLE IF EXISTS brand_sentiment_summary;
""")

cur.execute("""
CREATE TABLE brand_sentiment_summary AS
SELECT
    b.brand_name,
    sentiment,
    COUNT(*) AS total_mentions
FROM fact_mentions f
JOIN dim_brand b
ON f.brand_id = b.brand_id
GROUP BY b.brand_name, sentiment;
""")

conn.commit()

cur.close()
conn.close()

logging.info("Data mart updated successfully")

print("Data mart updated")