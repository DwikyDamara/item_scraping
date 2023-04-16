import scrapy
from scrapy import Request


class NflSpider(scrapy.Spider):
    name = "nfl"
    start_urls = ["https://www.nfl.com/players/"]

    def parse(self, response):
        # player = response.css(".d3-o-list__link::attr(href)").get()
        # link = response.urljoin(player + "stats")
        # yield Request(url=link, callback=self.parse_profile)
        popular_player = response.css(".d3-o-list__link::attr(href)").getall()
        for player in popular_player:
            link=response.urljoin(player+"stats")
            yield Request(url=link, callback=self.parse_profile)

    def parse_profile(self, response):
        link = response.urljoin("logs")
        yield Request(url=link, callback=self.parse_year)

    def parse_year(self,response):
        all_year = response.css("select option::text").getall()
        for year in all_year:
            link = response.urljoin(year)
            yield Request(url=link, callback=self.parse_log, meta={"year": year})

    def parse_log(self, response):
        year = response.meta["year"]
        player_name = response.css(".nfl-c-player-header__title::text").get()
        table = response.css("div.d3-l-grid--inner")
        if table:
            for i in table:
                season = i.css(".d3-o-section-sub-title::text").get()
                for data in i.css(".d3-o-table--horizontal-scroll>table>tbody>tr"):
                    week = data.css("td:nth-child(1)::text").get()
                    game_date = data.css("td:nth-child(2)::text").get()
                    opponent = data.css("td:nth-child(3)::text").get()
                    result = data.css("td:nth-child(4)::text").get()

                    item = {
                        "player_name": player_name,
                        "year": year,
                        "season": season,
                        "week": week,
                        "game_date": game_date,
                        "opponent": opponent,
                        "result": result
                    }
                    yield item
