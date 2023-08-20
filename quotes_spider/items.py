import scrapy


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()
    tags = scrapy.Field()


class AuthorItem(scrapy.Item):
    name = scrapy.Field()
    birthdate = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()
