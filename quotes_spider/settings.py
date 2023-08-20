BOT_NAME = 'quotes_spider'
SPIDER_MODULES = ['quotes_spider.spiders']
NEWSPIDER_MODULE = 'quotes_spider.spiders'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
    'quotes_spider.pipelines.QuotesJsonPipeline': 300,
    'quotes_spider.pipelines.AuthorsJsonPipeline': 400,
}



FEEDS = {
    'quotes.json': {
        'format': 'json',
        'store_empty': False,
        'encoding': 'utf8',
        'indent': 2,
    },
    'authors.json': {
        'format': 'json',
        'store_empty': False,
        'encoding': 'utf8',
        'indent': 2,
    },
}
