# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xml.etree.ElementTree as ET

class ScrapermetroPipeline(object):
    def process_item(self, item, spider):
        self.log(item)
