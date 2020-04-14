# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}']

    # 生成目的地址列表
    def parse(self, response):
        for index in range(0, 100 , 20):
            start_url = self.start_urls[0].format(index)
            print(start_url)
            yield scrapy.Request(
                url=start_url,
                callback=self.parse_movie_list
            )

    def parse_movie_list(self, response):

        json_data = json.loads(response.text)
        content_list = json_data["subjects"]
        for content in content_list:
            item = {}
            item["name"] = content["title"]
            item["href"] = content["url"]
            yield scrapy.Request(
                url=item["href"],
                callback=self.parse_movie_url,
                meta={"item": deepcopy(item)}
            )

    def parse_movie_url(self, response):

        item = response.meta["item"]
        response.xpath('').extract_first()


