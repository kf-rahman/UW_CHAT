import scrapy

class TextScraperSpider(scrapy.Spider):
    name = 'text_scraper'
    allowed_domains = ['uwaterloo.ca']
    start_urls = ['https://uwaterloo.ca/academic-calendar/undergraduate-studies/catalog#/programs/rJj6aXDk6']

    def parse(self, response):
        # XPath to extract all text from the page
        page_text = response.xpath('//body//text()').getall()
        page_text = [text.strip() for text in page_text if text.strip() != '']

        yield {
            'url': response.url,
            'text': ' '.join(page_text)
        }
