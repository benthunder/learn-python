import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        items = QuoteItem()
        all_div_quotes = response.css("div.quote")
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            items['title'] = title
            items['author'] = author
            items['tags'] = tags
            yield items
