from scrapy.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from alibaba.items import AlibabaItem 

import pymongo

class Alibaba_first_link_spider(CrawlSpider):
	name = "Alibaba_first_link"
	allowed_domains = []
	alphs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	start_urls = ['http://www.alibaba.com/countrysearch/IN/country/suppliers/a.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/b.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/c.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/d.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/e.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/f.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/g.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/h.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/i.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/j.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/k.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/l.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/m.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/n.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/o.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/p.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/q.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/r.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/s.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/t.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/u.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/v.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/w.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/x.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/y.html',
 'http://www.alibaba.com/countrysearch/IN/country/suppliers/z.html']
	# def start_requests(self):
	# 	for alph in self.alphs:
	# 		yield self.make_requests_from_url("http://www.alibaba.com/countrysearch/IN/country/suppliers/%s.html" % alph)
	
	rule = Rule(LinkExtractor(allow=(),restrict_xpath('.//a[@class="page_btn"]'),callback='parse_item',follow=True)

	# def make_start_urls(self):
	# 	for alph in self.alphs:
	# 		yield ("http://www.alibaba.com/countrysearch/IN/country/suppliers/%s.html" % alph)


	def parse_items(self, response):
		urls = Selector(response).xpath("//a[contains(@href,'suppliers_india')]")
		print len(urls)
		items = []
		for url in urls:
			item = AlibabaItem()
			item['url'] = str(url.xpath(".//@href").extract()[-1]).lstrip(" ").rstrip(" ")
			# print str(url.xpath(".//@href").extract()[-1]).lstrip(" ").rstrip(" ")
			item['industry_type'] = str(url.xpath(".//text()").extract()[-1]).strip("India")
			# print str(url.xpath(".//text()").extract()[-1]).strip("India")
			items.append(item)
			# yield items		
		return items	
