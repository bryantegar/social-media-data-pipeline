CREATE TABLE raw_news_mentions (
    id SERIAL PRIMARY KEY,
    brand TEXT,
    title TEXT,
    link TEXT,
    published_at TEXT,
    scraped_at TIMESTAMP
);

CREATE TABLE dim_brand (
    brand_id SERIAL PRIMARY KEY,
    brand_name TEXT UNIQUE
);

CREATE TABLE fact_mentions (
    mention_id SERIAL PRIMARY KEY,
    brand_id INT,
    title TEXT,
    link TEXT,
    published_at TEXT,
    scraped_at TIMESTAMP,
    sentiment TEXT,
    FOREIGN KEY (brand_id) REFERENCES dim_brand(brand_id)
);