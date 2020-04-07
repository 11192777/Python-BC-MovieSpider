# -*- coding: utf-8 -*-
import scrapy


class AiqiyiVidioSpider(scrapy.Spider):
    name = 'aiqiyi_vidio'
    allowed_domains = ['aiqiyi.cn']
    start_urls = ['https://list.iqiyi.com/www/1/-------------8-1-1-iqiyi--.html']

    def parse(self, response):
        # name = response.xpath('//p[@class="main"]/a/@title').extract()
        # grade = response.xpath('//p[@class="main"]/span/text()').extract()

        dataList = response.xpath('//p[@class="main"]')
        for data in dataList:
            item = {}
            item["name"] = data.xpath("./a/@title").extract_first()
            item["grage"] = data.xpath("./span/text()").extract_first()
            yield item
