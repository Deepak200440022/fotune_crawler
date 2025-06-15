import scrapy
from Quotes.items import QuotesItem

class QuoteSpider(scrapy.Spider):
    name = "quote"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        """
        @url https://quotes.toscrape.com/page/1/
        @returns items 10 10
        @returns request 1 50
        @scrapes quote author author_url
        """

        for Q in response.css("div.quote"):
            item = QuotesItem()
            item["quote"] = Q.css(".text::text").get()
            item["author"] = Q.css(".author::text").get()
            item["author_url"] = Q.css("span > a::attr(href)").get()
            yield item

        next_page = response.css(".next > a::attr(href)").get()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(url=next_page_url, callback=self.parse)