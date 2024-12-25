
# Books Web Scraper

This project is a web scraper built using the Scrapy framework. It crawls the [Books to Scrape](http://books.toscrape.com/) website to extract product details such as name, price, rating, and availability. The extracted and cleaned data is stored in a MongoDB database.

---

## Overview

The scraper performs the following tasks:
1. Crawls the website to extract:
   - Product Name
   - Price
   - Rating
   - Availability
2. Cleans and processes the extracted data:
   - Converts price to float
   - Maps ratings to numerical values
   - Standardizes availability to "In Stock" or "Out of Stock"
3. Stores the processed data into a MongoDB database with the schema:
   - `product_name` (string)
   - `price` (float)
   - `rating` (float)
   - `availability` (string)

---

## Setup and Running the Scraper

### Prerequisites
- Python 3.7 or above
- MongoDB installed and running locally
- pip (Python package manager)
- **Scrapy**: For web scraping.
- **pymongo**: To interact with MongoDB.
- **Rust Compiler**: Required for building certain Python packages (e.g., cryptography).

---

### Installation

1. Clone the repository:
   ```bash
   git clone <your-forked-repo-url>
   cd <your-repo-directory>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install scrapy pymongo
   ```

4. Ensure MongoDB is running locally 
  
  



### Running the Crawler

1. Navigate to the project directory:
   ```bash
   cd bookscraper
   ```

2. Run the Scrapy spider:
   ```bash
   scrapy crawl books_spider
   ```

3. Check MongoDB Compass to verify the scraped data in the `books_database` under the `products` collection.

---

## Dependencies
- **Scrapy**: For web crawling and data extraction.
- **pymongo**: To interact with MongoDB.
- **Rust**: Required for certain Python dependencies (e.g., cryptography).




