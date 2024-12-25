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


