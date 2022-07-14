import scrapy
import w3lib.html


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        # getting data using css method
        # title=response.css('span.title::text').get()
        # getting data using xpath method
        # author = response.xpath('//span[@class="author-name"]/text()').get
        # title = response.xpath('//span[@class="title"]/text()').get()
        
        
        return {
            w3lib.html.remove_tags(response.xpath('//div[@class="text"]').get())
        }

