# -*- coding: utf-8 -*-
import scrapy
from snyg.items import SnygItem
from copy import deepcopy

class SnbSpider(scrapy.Spider):
    name = 'snb'
    allowed_domains = ['list.suning.com']
    start_urls = ['https://book.suning.com/']

    start_urls = ['https://list.suning.com/1-264003-0.html']

    def parse(self, response):
        # item = SnygItem() #类字典
        booklist = response.xpath('//*[@id="filter-results"]/ul/li')
        for i in booklist:
            item = SnygItem()  # 类字典
            item['price'] = i.xpath('.//*[@class="res-info"]/p[1]/em/@class').extract_first()
            item['title'] = i.xpath('.//*[@class="res-info"]/p[2]/a/text()').extract_first()
            item['href'] = i.xpath('.//*[@class="res-info"]/p[2]/a/@href').extract_first()
            item['salesname'] = i.xpath('.//*[@class="res-info"]/p[4]/a/text()').extract_first()
            # yield item

            # href = "http:"+item['href']
            # log
            # '2018-07-31 00:07:59 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) '\
            # 'to <GET https://product.suning.com/0070091573/102097960.html> from ' \
            # '<GET http://product.suning.com/0070091573/102097960.html>'

            href = "https:"+item['href']
            yield scrapy.Request(href, callback=self.parse_detail, meta={"item": item}, dont_filter=True)
            # yield scrapy.Request(href, callback=self.parse_detail, meta={"item": deepcopy(item)}, dont_filter=True)
        for xx in range(1,3):
            next_url = 'https://list.suning.com/1-264003-{}-0-0-0-0-0-0-4.html'.format(xx)
            # print(next_url)
            yield scrapy.Request(next_url,callback=self.parse)
    def parse_detail(self,response):
        item = response.meta["item"]
        # item['desc']='hhh99999999999999999999999999999999999999'
        item['desc']=response.xpath('//*[@id="bookconMain"]/dl[2]/dd/p/text()').extract_first()
        # if item['desc']==None:  #书籍介绍为图片
            # print(item)
            # print('*'*100,item['href'])
        yield item

