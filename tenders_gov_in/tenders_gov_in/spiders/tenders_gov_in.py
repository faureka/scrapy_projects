from scrapy.spiders import BaseSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
#from tenders_gov_in.items import TendersGovInItem

class tenders_gov_in_data(BaseSpider):
	name = "tenders"
	allowed_domains = []
	
	def __init__(self,filename=None):
		if filename:
			with open(filename,"r+") as f:
				self.start_urls = f.readlines()
	def parse(self,response):
		dict_data = {}
		dom_table = Selector(response).xpath("//table[@class='TabBrdLess']//form//tr")
		for elems in dom_table:
			elem = elems.xpath(".//td/text()").extract()
			if len(elem) > 1:
				dict_data[elem[0].encode('utf-8').replace(".","")] = elem[1].encode('utf-8')
		return dict_data	 	


