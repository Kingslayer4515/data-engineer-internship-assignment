# Data Engineering Internship Assignment

Welcome to the Data Engineering Internship Assignment! This task is designed to evaluate your problem-solving skills, understanding of data pipelines, and ability to work with web crawling and data extraction. Please read the instructions carefully and submit your solution as per the guidelines provided.

## Problem Statement

You are tasked with building a basic web crawling pipeline to extract and process data from a target website. The goal is to:

1. **Crawl** a given webpage to extract specific information.
2. **Clean and process** the extracted data.
3. **Store** the processed data into a MongoDB database.

### Target Website

You will be working with the Books to Scrape website (http://books.toscrape.com/) or any other publicly accessible e-commerce website containing product information. Ensure that your crawler abides by the website's `robots.txt` policy.

### Tasks

#### Step 1: Web Crawling

1. Use the `Scrapy` framework to:
   - Fetch the HTML content of the target webpage.
   - Extract product details such as:
     - `Product Name`
     - `Price`
     - `Rating`
     - `Availability Status`

#### Step 2: Data Transformation

1. Clean the extracted data (e.g., remove extra whitespace, convert prices to float, handle missing ratings).
2. Standardize the data (e.g., convert availability status to `In Stock` or `Out of Stock`).

#### Step 3: Data Storage

1. Store the processed data into a MongoDB database.
2. Use a collection named `products` with the following schema:
   - `product_name` (string)
   - `price` (float)
   - `rating` (float)
   - `availability` (string)

#### Step 4: Documentation

Prepare a `README.md` file that includes:
1. An overview of your solution.
2. Steps to set up and run your crawler.
3. Dependencies and setup instructions.

#### Step 5: Git Guidelines

1. Use meaningful commit messages.
2. Follow a proper branch naming convention (e.g., `feature/<your_name>`).
3. Ensure your code is clean, modular, and well-commented.

## Submission Guidelines

1. Fork this repository.
2. Create a new branch named `submission/<your_name>`.
3. Commit your code and push it to your forked repository.
4. Create a Pull Request (PR) to the `main` branch of this repository.
5. Include your `README.md` and ensure your code is well-documented.

## Evaluation Criteria

1. **Correctness**: Does your solution meet the requirements?
2. **Code Quality**: Is your code clean, modular, and well-documented?
3. **Efficiency**: Are the crawling and transformations optimized?
4. **Git Practices**: Are proper git guidelines followed?

---

Good luck! We look forward to reviewing your submission.
