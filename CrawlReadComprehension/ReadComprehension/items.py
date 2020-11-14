# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item, Field

class ReadcomprehensionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class Economist(Item):
    newsId = Field()
    content = Field()
    theme = Field()
    keywords = Field()
    paragraphs = Field()
    sentence = Field()
    wordCount = Field()
    superClassWord = Field()
    difficulty = Field()
    title = Field()
    date = Field()

