import requests
import pandas as pd
import xml.etree.ElementTree as ET
from datetime import datetime
import logging

logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

brands = [
    "Telkomsel",
    "Gojek",
    "Tokopedia",
    "Shopee",
    "Samsung"
]

all_data = []

for brand in brands:

    url = f"https://news.google.com/rss/search?q={brand}&hl=id&gl=ID&ceid=ID:id"

    response = requests.get(url)

    root = ET.fromstring(response.content)

    for item in root.findall(".//item"):

        title = item.find("title").text
        link = item.find("link").text
        pub_date = item.find("pubDate").text

        all_data.append({
            "brand": brand,
            "title": title,
            "link": link,
            "published_at": pub_date,
            "scraped_at": datetime.now()
        })

df = pd.DataFrame(all_data)

logging.info(f"Scraping completed. Total articles scraped: {len(df)}")

print("Total articles scraped:", len(df))
print(df.head())

df.to_csv("news_data.csv", index=False)