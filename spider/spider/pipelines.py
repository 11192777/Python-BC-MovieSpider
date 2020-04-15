# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SpiderPipeline(object):

    def __init__(self):
        self.file_index = 0
        self.file_size = 0


    def process_item(self, item, spider):
        filename = 'G:/豆瓣电影/douban_movies_discuss_{}.txt'.format(self.file_index)
        with open(filename, 'a') as file:
            str = "{}_{}_{}_{}_{}\n".format(item["name"], item["level"], item["href"], item["user_url"], item["user_id"])
            file.write(str)
            self.file_size += 1

        if (self.file_size >= 100):
            self.file_index += 1
            self.file_size = 0


