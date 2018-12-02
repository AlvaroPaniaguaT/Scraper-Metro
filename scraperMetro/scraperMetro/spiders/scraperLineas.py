# -*- coding: utf-8 -*-
import scrapy
from scraperMetro.items import ScrapermetroItem as SMI
from scrapy.loader import ItemLoader


class ScraperlineasSpider(scrapy.Spider):
    name = 'scraperLineas'
    allowed_domains = ['www.metromadrid.es']
    start_urls = ['http://www.metromadrid.es']

    def parse(self, response):
        # extract station names
        for line in response.xpath("//*[@id='block-metro-network-status-block']/div/ul/li"):
            item_loader = ItemLoader(item=SMI(), selector=line)
            item_loader.add_xpath('line', ".//a/img/@class")
            yield item_loader.load_item()

            # extract extension url paths to different lines
        next_page = response.xpath("//*[@id='block-metro-network-status-block']/div/ul/li/a/@href").extract_first()
        if next_page is not None:
            next_page_link = response.urljoin(next_page)
            yield response.follow(url=next_page_link, callback=self.parse_stations)

    def parse_stations(self, response):
        for station in response.xpath("//*[@id='line-main']/ul/li"):
            item_loader = ItemLoader(item=SMI(), selector=station)
            item_loader.add_xpath('station', './/a/p/text()')
            yield item_loader.load_item()

