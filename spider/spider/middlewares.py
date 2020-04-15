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
    def process_request(self, request, spider):
        request.meta['proxy'] = 'http://58.19.83.94'

