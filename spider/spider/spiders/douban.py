# -*- coding: utf-8 -*-
import scrapy
import json
from copy import deepcopy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start={}']

    # 生成目的地址列表
    def parse(self, response):

        for index in range(0, 40, 20):
            start_url = self.start_urls[0].format(index)
            print(start_url)
            yield scrapy.Request(
                url=start_url,
                callback=self.parse_movie_list
            )

    # 获取目的地址列表网页中每一个电影的url
    def parse_movie_list(self, response):

        json_data = json.loads(response.text)
        content_list = json_data["subjects"]
        for content in content_list:
            item = {}
            item["name"] = content["title"]
            item["href"] = content["url"]
            yield scrapy.Request(
                item["href"],
                callback=self.parse_movie_url,
                meta={"item": deepcopy(item)}
            )

    # 进入每一个电影的url，并找到用户评论区的目的地址
    def parse_movie_url(self, response):

        item = response.meta["item"]
        item["discuss"] = item["href"] + "reviews"

        yield scrapy.Request(
            url=item["discuss"],
            callback=self.parse_users_discuss,
            meta={"item": deepcopy(item)}
        )

    # 进入用户评论区
    def parse_users_discuss(self, response):

        last_item = response.meta["item"]

        discuss_list = response.xpath('//div[@class="main review-item"]/header')

        for discuss in discuss_list:
            item = {}
            item["name"] = last_item["name"]
            item["level"] = discuss.xpath('.//span/@title').extract()
            item["href"] = last_item["href"]
            item["user_name"] = discuss.xpath('.//a[2]/text()').extract()
            item["user_url"] = discuss.xpath('.//a[1]/@href').extract()

            yield scrapy.Request(
                url=item["user_url"][0],
                callback=self.parse_users_id,
                meta={"item": deepcopy(item)}
            )

    # 获取用户的真实id
    def parse_users_id(self, response):
        item = response.meta["item"]
        item["user_id"] = response.xpath('//div[@class="aside"]//div[@class="user-info"]/div').extract()

        yield item
