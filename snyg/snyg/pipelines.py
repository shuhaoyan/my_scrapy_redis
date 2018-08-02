# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#-----自己改写---

# log 日志信息输出
# import json
# import logging
# logger = logging.getLogger(__name__)

#数据库引入
from pymongo import MongoClient


class SnygPipeline(object):
    # def open_spider(self,spider):
    #     MONGO_HOST = spider.settings.get('MONGO_HOST')  #从配置文件获取配置信息
    #     client = MongoClient(MONGO_HOST)
    #     self.clloection = client["syng"]["book"]  #数据库syng--表book

    # def process_item(self, item, spider):
    #     return item   # 显示return 控制台输出
    #     # pass

    def process_item(self, item, spider):
        # item['content'] = self.process_content(item['content'])
        # self.clloection.insert(dict(item))   #类字典对象转化为字典对象，存储到mongodb数据库
        # self.clloection.update({'title': dict(item)['title']}, {'$set': dict(item)}, True)  # 类字典对象转化为字典对象，存储到mongodb数据库
        return item   # 显示return 控制台输出
        # logger.warning(item)# log 日志信息输出


    # def process_content(self, content):
    #     # content = content.replace('\xa0','')
    #     content = re.sub(r'\xa0|\s', "", content)
    #     return content