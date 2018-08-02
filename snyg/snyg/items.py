# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SnygItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    price = scrapy.Field()
    title = scrapy.Field()
    href = scrapy.Field()
    salesname = scrapy.Field()
    desc = scrapy.Field()


    pass
