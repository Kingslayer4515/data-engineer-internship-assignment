import scrapy

class BooksSpider(scrapy.Spider):
    name = "books_spider"
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        for book in response.css('article.product_pod'):
            # Extract data
            product_name = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            rating = book.css('p::attr(class)').re_first('star-rating (\w+)')
            availability_raw = book.css('p.instock.availability::text').getall()

            # Clean and process availability
            availability = ''.join(availability_raw).strip()  # Combine all text and strip spaces

            yield {
                'product_name': product_name,
                'price': price,
                'rating': rating,
                'availability': availability,
            }

        # Handle pagination
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
