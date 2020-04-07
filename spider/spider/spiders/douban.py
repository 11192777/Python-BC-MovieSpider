# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0']
    start_urls = ['https://movie.douban.com/explore#!type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=rank&page_limit=20&page_start=0']

    def parse(self, response):
        print(response)
