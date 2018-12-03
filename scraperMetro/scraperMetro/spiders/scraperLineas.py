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
            line_name = line.xpath(".//a/img/@class").extract_first()
            self.log(line_name)
            # extract extension url paths to different lines
            next_page = line.xpath(".//a/@href").extract_first()
            if next_page is not None:
                next_page_link = response.urljoin(next_page)
                yield response.follow(url=next_page_link, callback=self.parse_stations, meta={ 'line_name': line_name })


    def parse_stations(self, response):
        item = SMI()
        item['line'] = response.meta['line_name']
        for station in response.xpath("//*[@id='line-main']/ul/li"):
            item['station'] = station.xpath(".//a/p/text()").extract_first()
            info_list = station.xpath(".//*[@id]/div/div/div/div/div/div/div/div/span/text()").extract()
            if "Estación accesible" in info_list:
                item['accesible'] = True
            else:
                item['accesible'] = False

            if "Ascensores" in info_list:
                item['elevator'] = True
            else:
                item['elevator'] = False

            if "Escaleras Mecánicas" in info_list:
                item['mechanic_stairs'] = True
            else:
                item['mechanic_stairs'] = False

            yield item
