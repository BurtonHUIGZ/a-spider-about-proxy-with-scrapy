# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    HOST = scrapy.Field()#ip地址
    POST = scrapy.Field()#端口号
    survivingTime = scrapy.Field()#存活时间
    address = scrapy.Field()#服务器地址
    checkTime = scrapy.Field()#验证时间
