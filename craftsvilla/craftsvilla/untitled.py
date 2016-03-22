import scrapy.Spider as Spiders
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from craftsvilla.items import CraftsvillaItem 

import pymongo

class Crafts_Villa(Spiders):
	"""docstring for Crafts_Villa"""
	name = "Company_details"
	allowed_domains = []

	def __init__(self,filename=None):
		if filename:
			with open(filename,'r') as f:
				self.start_urls = f.readlines().strip()

	def parse(self, response):
		item = CraftsvillaItem()
		sel = Selector(response).xpath("//span[@class='dtlLink-select']//span//text()").extract()[0:2]
		name_comp = Selector(response).xpath("//div[@class='vendorNameHead']//h1//text()").extract().encode("utf-8","ignore").strip()
		item['pageviews'] = sel[1].strip().split(":")[1].encode("utf-8","ignore")
		item['address']	= sel[0].strip().encode("utf-8","ignore")		
		item['_id'] = name_comp