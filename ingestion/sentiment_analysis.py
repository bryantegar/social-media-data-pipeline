import psycopg2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

analyzer = SentimentIntensityAnalyzer()

conn = psycopg2.connect(
    host="localhost",
    database="social_media_pipeline",
    user="postgres",
    password="postgres"
)

cur = conn.cursor()

cur.execute("SELECT mention_id, title FROM fact_mentions")

rows = cur.fetchall()

for row in rows:

    mention_id = row[0]
    title = row[1]

    score = analyzer.polarity_scores(title)

    if score["compound"] >= 0.05:
        sentiment = "positive"
    elif score["compound"] <= -0.05:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    cur.execute(
        "UPDATE fact_mentions SET sentiment=%s WHERE mention_id=%s",
        (sentiment, mention_id)
    )

conn.commit()

logging.info("Sentiment analysis completed")

cur.close()
conn.close()

print("Sentiment analysis completed")