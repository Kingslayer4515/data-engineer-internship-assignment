import pymongo

class BooksScraperPipeline:
    def __init__(self):
        # MongoDB setup
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["books_database"]
        self.collection = self.db["products"]

    def process_item(self, item, spider):
        # Clean and process the product_name
        item['product_name'] = item['product_name'].strip() if item['product_name'] else "Unknown Product"

        # Clean and convert the price to float
        if item['price']:
            item['price'] = float(item['price'].replace('£', '').strip())
        else:
            item['price'] = 0.0  # Default to 0.0 if the price is missing

        # Convert rating to float
        rating_map = {'One': 1.0, 'Two': 2.0, 'Three': 3.0, 'Four': 4.0, 'Five': 5.0}
        item['rating'] = rating_map.get(item['rating'], 0.0)  # Default to 0.0 if rating is missing

        # Clean and standardize availability
        raw_availability = item['availability'].lower() if item['availability'] else ''
        item['availability'] = 'In Stock' if 'in stock' in raw_availability else 'Out of Stock'

        # Insert the cleaned and processed item into MongoDB
        self.collection.insert_one({
            "product_name": item['product_name'],
            "price": item['price'],
            "rating": item['rating'],
            "availability": item['availability']
        })
        return item

    def close_spider(self, spider):
        # Close the MongoDB connection
        self.client.close()
