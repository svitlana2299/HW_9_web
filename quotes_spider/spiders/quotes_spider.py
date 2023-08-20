import scrapy
from ..items import QuoteItem, AuthorItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["http://quotes.toscrape.com/page/1/"]

    def parse(self, response):
        for quote in response.xpath("//div[@class='quote']"):
            text = quote.xpath(".//span[@class='text']/text()").get()
            author_name = quote.xpath(".//small[@class='author']/text()").get()
            tags = quote.xpath(
                ".//div[@class='tags']/a[@class='tag']/text()").getall()

            yield QuoteItem(text=text, author=author_name, tags=tags)

            author_url = quote.xpath(
                ".//small[@class='author']/following-sibling::a/@href").get()
            yield response.follow(author_url, self.parse_author)

        next_page = response.xpath("//li[@class='next']/a/@href").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        name = response.xpath("//h3[@class='author-title']/text()").get()
        birthdate = response.xpath(
            "//span[@class='author-born-date']/text()").get()
        born_location = response.xpath(
            "//span[@class='author-born-location']/text()").get()
        description = response.xpath(
            "//div[@class='author-description']/text()").get()

        yield AuthorItem(name=name, birthdate=birthdate, born_location=born_location, description=description)
