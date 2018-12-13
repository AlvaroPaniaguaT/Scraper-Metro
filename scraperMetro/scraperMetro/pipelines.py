# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xml.etree.ElementTree as ET

class ScrapermetroPipeline(object):

    def open_spider(self, spider):
        # Poner Path a los KML del equipo local
        self.file_metro = ET.parse('/home/alvaro/Escritorio/Máster-DataScience/Obtencion-De-Datos/Scraper-Metro/scraperMetro/scraperMetro/Metro_2018_11.kml')
        self.file_metro_l = ET.parse('/home/alvaro/Escritorio/Máster-DataScience/Obtencion-De-Datos/Scraper-Metro/scraperMetro/scraperMetro/MetroLigero_2018_11.kml')
        self.root = self.file_metro.getroot()
        self.root2 = self.file_metro_l.getroot()

        self.stations = self.root.findall(".//{http://www.opengis.net/kml/2.2}Placemark/{http://www.opengis.net/kml/2.2}name")
        print(len(self.stations))
        self.stations += self.root2.findall(".//{http://www.opengis.net/kml/2.2}Placemark/{http://www.opengis.net/kml/2.2}name")

        self.coordinates = self.root.findall(".//{http://www.opengis.net/kml/2.2}Placemark/{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates")
        print(len(self.coordinates))
        self.coordinates += self.root2.findall(".//{http://www.opengis.net/kml/2.2}Placemark/{http://www.opengis.net/kml/2.2}Point/{http://www.opengis.net/kml/2.2}coordinates")

    def process_item(self, item, spider):
        for pos, station in enumerate(self.stations):
            if item['station'].upper() == "ARGÜELLES":

                print(item['station'].upper(), station.text)
            if item['station'].upper() in station.text:
                item['coordinates'] = self.coordinates[pos].text.replace("\n", " ").split(",")
                break

        return item
