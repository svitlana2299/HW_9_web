from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from quotes_spider.spiders.quotes_spider import QuotesSpider


# Створюємо екземпляр об'єкта CrawlerProcess з налаштуваннями проекту
process = CrawlerProcess(get_project_settings())

process.crawl(QuotesSpider)

# Запускаємо процес скрапінгу
process.start()
