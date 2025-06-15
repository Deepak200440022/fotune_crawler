# Fortune Crawler

A Python-based scraper and viewer for motivational quotes from [quotes.toscrape.com](https://quotes.toscrape.com/page/1/), using Scrapy to crawl, MongoDB to store, and a CLI tool to display a random quote.

---

## 🔍 Overview

This project provides:

- A **Scrapy spider** to scrape quotes from [quotes.toscrape.com](https://quotes.toscrape.com/page/1/).
- A **MongoDB pipeline** to persist the scraped data.
- A **standalone Python script** to display a random quote from the MongoDB collection in the terminal.

Example quote document:

```json
{
  "_id": "70bfc7c998276705ce55e83ed00fe53725f15379c75e55c7d909e3bd1f82120c",
  "author": "Ralph Waldo Emerson",
  "author_url": "/author/Ralph-Waldo-Emerson",
  "quote": "“For every minute you are angry you lose sixty seconds of happiness.”"
}
````

---

## 📁 Project Structure

```
web_scraper/
├── scrapy.cfg
├── web_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   └── spiders/
│       ├── __init__.py
│       └── quote.py         # Spider scraping quotes.toscrape.com
├── fortuneJr.py          # CLI script: print a random quote from MongoDB
```

---

## ⚙️ Setup Instructions

### 1. Install Dependencies

```bash
pip install scrapy pymongo
```

### 2. Start MongoDB

Ensure MongoDB is installed and actively listening at `localhost:27017`.

### 3. Scrape Quotes

Use the following command to crawl and store quotes:

```bash
scrapy crawl quote
```

### 4. View a Random Quote

Run this script to see a random quote:

```bash
python fetch_random.py
```

If the database is empty, the script will prompt you to run the crawler.

---

## 🔧 Configuration

In `settings.py`, define:

```python
MONGO_URI = "mongodb://localhost:27017"
MONGO_DATABASE = "quotes_db"
```

The spider stores quotes in a collection named after the spider (`quote`).

---

## 📝 Example Output

```bash
{'quote': '“For every minute you are angry you lose sixty seconds of happiness.”', 'author': 'Ralph Waldo Emerson', 'author_url': '/author/Ralph-Waldo-Emerson'}
```

---

## ⚠️ Notes

* Quotes are scraped from [https://quotes.toscrape.com/page/1/](https://quotes.toscrape.com/page/1/).
* Use only for educational, research, or personal purposes.
* MongoDB must be running before using the crawler or viewer.

---

```
```
