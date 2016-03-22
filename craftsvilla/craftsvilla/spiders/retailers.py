from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

# from craftsvilla.items import CraftsvillaItem 
import pymongo

# class Craftsvilla(object):
# 	"""docstring for Craftsvilla"""
# 	name = "Craftsvillaspider"
# 	allowed_domains = []
# 	start_url = ["http://www.craftsvilla.com/jewellery-jewelry.html"]
# 	rules = (Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@title="Next"]',)), callback="parse_items", follow= True),)
