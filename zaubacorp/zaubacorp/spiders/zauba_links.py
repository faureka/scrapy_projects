from scrapy.spiders import CrawlSpider,Rule,BaseSpider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector,Request
from zaubacorp.items import ZaubacorpItem

# '''
# name = scrapy.Field()
# url = scrapy.Field()
# roc_data = scrapy.Field()
# status = scrapy.Field()
# _id = scrapy.Field()
# reg_num = scrapy.Field()
# comp_cat = scrapy.Field()
# comp_sub_cat = scrapy.Field()
# comp_class = scrapy.Field()
# auth_cap = scrapy.Field()
# paid_up_cap = scrapy.Field()
# no_members = scrapy.Field()
# date_incorp = scrapy.Field()
# email = scrapy.Field()
# website = scrapy.Field()
# addr1 = scrapy.Field()
# addr2 = scrapy.Field()
# city = scrapy.Field()
# state = scrapy.Field()
# country = scrapy.Field()
# pin = scrapy.Field()
# activity = scrapy.Field()								#listed or unlisted
# date_AGM = scrapy.Field()
# date_bal_sheet = scrapy.Field()


# '''




import pymongo
class ZaubacorpLinks(BaseSpider):
		name = "ZaubacorpLinks"f
		allowed_domains = []
		base_url  = 'https://www.zaubacorp.com/company-list/p-'
		extension_url = '-company.html'
		start_urls = [base_url+str(i)+extension_url for i in xrange(1,52247)]
    # def start_requests(self):
    #       for alph in self.alphs:
    #               yield self.make_requests_from_url("http://www.alibaba.com/countrysearch/IN/country/suppliers/%s.html" % alph)

    # rule = Rule(LinkExtractor(allow=(),restrict_xpath('.//a[@class="page_btn"]'),callback='parse_item',follow=True)

    # def make_start_urls(self):
    #       for alph in self.alphs:
    #               yield ("http://www.alibaba.com/countrysearch/IN/country/suppliers/%s.html" % alph)
		def parse_start_urls(self,response):
			return self.parse(response)

    	
		def parse_listing(self,response):
			item = response.meta['item']
			rows_data = Selector(response).xpath(".//table/tr")
		# for row in rows_data:
			# print row.xpath("./td")[1].xpath(".//text()").extract()[0].encode("utf-8","ignore")
			item['reg_num'] = rows_data[3].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['comp_cat'] = rows_data[5].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")	
			item['comp_sub_cat'] = rows_data[6].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['comp_class'] = rows_data[7].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['auth_cap'] = self.tofloat(rows_data[8].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore"))
			item['paid_up_cap'] = self.tofloat(rows_data[9].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore"))
			item['no_members'] = rows_data[10].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['date_incorp'] = rows_data[11].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['email'] = rows_data[12].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['website'] = rows_data[13].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['addr1'] = rows_data[14].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['addr2'] = rows_data[15].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['city'] = rows_data[16].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['state'] = rows_data[17].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['country'] = rows_data[18].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['pin'] = rows_data[19].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['activity'] = rows_data[20].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['date_AGM'] = rows_data[21].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")
			item['date_bal_sheet'] = rows_data[22].xpath("./td")[1].xpath(".//p//text()").extract()[0].encode("utf-8","ignore")

			return item
    	# print response.url


		def parse(self, response):
			rows = Selector(response).xpath(".//table[@id='table']/tr")
			for row in rows:
				item = ZaubacorpItem()
				items = row.xpath("./td")
				item['url'] = items[1].xpath(".//@href").extract()[0].encode("utf-8",'ignore')
				item['roc_data'] = items[2].xpath(".//text()").extract()[0].encode("utf-8",'ignore')
				item['status'] = items[3].xpath(".//text()").extract()[0].encode("utf-8",'ignore')
				item['_id'] = items[0].xpath(".//text()").extract()[0].encode("utf-8",'ignore')
				item['name'] = items[1].xpath(".//text()").extract()[0].encode("utf-8",'ignore')
				request = Request(item['url'],callback=self.parse_listing)
				request.meta['item'] = item
				# print str(url.xpath(".//@href").extract()[-1]).lstrip(" ").rstrip(" ")
				# print str(url.xpath(".//text()").extract()[-1]).strip("India")
				return request
        
		def tofloat(self,number):
			try:	
				number = float(number.replace(",",""))    
				return number	    	     
			except ValueError:
				return	



# print len(urls)
# items = []
