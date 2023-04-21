import scrapy


class AzdirectSpider(scrapy.Spider):
    name = "azdirect"
    start_urls = ["https://azdirect.az.gov/agencies"]

    def parse(self, response):
        table = response.css(".view-content .table-responsive table tbody tr")
        for content in table:
            agency_name = content.css("td a::text").get()
            agency_link = content.css("td:nth-child(2) a::attr(href)").get()
            address = content.css(".views-field-field-address *::text").getall()
            yield {
                "agency name": agency_name,
                "agency link": agency_link,
                "address": address
            }
        # table = response.css(".agencytitle")
        # for content in table:
        #     agency_name = content.css("a::text").get()
        #     yield {
        #         "agency name": agency_name,
        #     }