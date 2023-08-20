import json


class QuotesJsonPipeline:
    def open_spider(self, spider):
        self.quotes = []

    def close_spider(self, spider):
        with open('quotes.json', 'w', encoding='utf-8') as file:
            json.dump(self.quotes, file, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        quote = {
            'tags': item.get('tags', []),
            'author': item.get('author', ''),
            'quote': item.get('quote', ''),
        }
        self.quotes.append(quote)
        return item


class AuthorsJsonPipeline:
    def open_spider(self, spider):
        self.authors = []

    def close_spider(self, spider):
        with open('authors.json', 'w', encoding='utf-8') as file:
            json.dump(self.authors, file, ensure_ascii=False, indent=2)

    def process_item(self, item, spider):
        self.authors.append({
            'fullname': item['name'],
            'born_date': item['birthdate'],
            'born_location': item['born_location'],
            'description': item['description']
        })
        return item
