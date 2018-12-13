# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapermetroItem(scrapy.Item):
    # define the fields for your item here like:
    line = scrapy.Field()
    station = scrapy.Field()
    accesible = scrapy.Field()
    elevator = scrapy.Field()
    mechanic_stairs = scrapy.Field()
    coordinates = scrapy.Field()
    url_linea = scrapy.Field()
