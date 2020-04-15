# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64
from scrapy.utils.python import to_bytes


class SpiderProxysSetting(object):
    def __init__(self):
        self.proxys = ['http://58.19.83.94:80',
                       'http://182.126.53.121:80',
                       'http://115.210.70.25:80',
                       'http://101.205.164.60:80',
                       'http://180.124.230.162:80',
                       'http://171.80.184.58:80',
                       'http://116.55.124.162:80']

        print("---------------------------------")

    def process_request(self, request, spider):
        print("+++++++++++++++++++++++++++++++")
        request.meta['proxy'] = self.proxys[random.randint(0, len(self.proxys))]
        pass
