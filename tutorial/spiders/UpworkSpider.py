import scrapy
from tutorial.items import UpworkItem

class UpworkSpider(scrapy.Spider):
    name = "upwork"
    allowed_domains = ["upwork.com"]
    start_urls = [
            "https://www.upwork.com/o/jobs/browse/?q=python"
            ]

    def parse(self, response):
        for article in response.css("article"):
            item = UpworkItem()
            item['title'] = article.xpath('header/h2/a/text()').extract().strip()
            yield item 

    # def parse_dir_contents(self, response):
    #     for sel in response.xpath('//ul/li'):
    #         item = DmozItem()
    #         item['title'] = sel.xpath('a/text()').extract()
    #         item['link'] = sel.xpath('a/@href').extract()
    #         item['desc'] = sel.xpath('text()').extract()
    #         yield item
