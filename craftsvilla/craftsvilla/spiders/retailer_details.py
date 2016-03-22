from scrapy import Spider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from craftsvilla.items import CraftsvillaItem 

import pymongo

# class Craftsvilla(CrawlSpider):
# 	name = "Craftsvillaspider"
# 	allowed_domains = []
# 	start_urls = ['http://www.craftsvilla.com/sarees-sari.html']
# 	rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@title="Next"]',)), callback="parse_items", follow= True),)
# 	print "###################################################"
# 	# rule = Rule(LinkExtractor(allow=(),restrict_xpath('.//a[@title="Next"]')),callback='parse_item',follow=True)
# 	# rules = [Rule(LinkExtractor(allow=(),restrict_xpath('.//a[@title="Next"]')),
# 	# # 	callback='parse_item', follow=True)]
# 	# rules = [
#  #    Rule(LinkExtractor(allow=(),restrict_xpath(".//a[@title='Next']")),
#  #         callback='parse_item', follow=True)
#  #    ]


# 	def parse_items(self,response):
# 		fields = Selector(response).xpath(".//p[@class ='vendorname']//a")
# 		items = set()
# 		print "1"
# 		print len(fields)
# 		for elems in fields:
# 			item = CraftsvillaItem()
# 			try:
# 				item['url'] = elems.xpath(".//@href").extract()[0].encode('utf-8','ignore')
# 				item['name'] = elems.xpath(".//text()").extract()[0].encode('utf-8','ignore')
# 			except Exception, e:
# 				print e
# 				continue

# 			# print elems.xpath(".//@href").extract()
# 			items.add(item)
# 			# print list(items)	
# 		return list(items)
# 			# return		



# 	# def parse_items(self, response):
# 	# 		urls = Selector(response).xpath("//a[contains(@href,'suppliers_india')]")
# 	# 		print len(urls)
# 	# 		items = []
# 	# 		for url in urls:
# 	# 			item = AlibabaItem()
# 	# 			item['url'] = str(url.xpath(".//@href").extract()[-1]).lstrip(" ").rstrip(" ")
# 	# 			# print str(url.xpath(".//@href").extract()[-1]).lstrip(" ").rstrip(" ")
# 	# 			item['industry_type'] = str(url.xpath(".//text()").extract()[-1]).strip("India")
# 	# 			# print str(url.xpath(".//text()").extract()[-1]).strip("India")
# 	# 			items.append(item)
# 	# 		# yield items		
# 	# return items	

class Craftsvilla(Spider):
	"""docstring for Crafts_Villa"""
	name = "Company_details"
	allowed_domains = []
	f = open("links.txt")
	start_urls = [url.strip() for url in f.readlines()]

	# def __init__(self,filename=None):
	# 	if filename:
	# 		with open(filename,'r') as f:
	# 			self.start_urls = f.readline().strip()

	def parse(self, response):
		item = CraftsvillaItem()
		sel = Selector(response).xpath("//span[@class='dtlLink-select']//span//text()").extract()[0:2]
		name_comp = Selector(response).xpath("//div[@class='vendorNameHead']//h1//text()").extract()[0].encode("utf-8","ignore").strip()
		item['pageviews'] = sel[1].strip().split(":")[1].encode("utf-8","ignore")
		item['address']	= sel[0].strip().encode("utf-8","ignore")		
		item["_id"] = name_comp
		self.state['item_count']  = self.state.get('items_count', 0) + 1
		return item