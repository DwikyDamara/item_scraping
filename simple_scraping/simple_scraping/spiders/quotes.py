import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.css(".quote")
        for quote in quotes:
            author = quote.css(".author::text").get()
            text = quote.css(".text::text").get()
            tags = quote.css(".tag::text").getall()
            yield {
                "author" : author,
                "quote" : text,
                "tags" : tags
            }
