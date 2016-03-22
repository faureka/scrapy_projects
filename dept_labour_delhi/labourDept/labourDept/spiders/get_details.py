from scrapy.spiders import CrawlSpider,Rule,BaseSpider
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector,Request
from labourDept.items import LabourdeptItem
import pymongo
import re

conn = pymongo.MongoClient("localhost",27017)
db = conn['Zoukloans']
coll = db["labourDeptlinks"]
# contact_regex = re.compile(r'')

# regNumber = scrapy.Field()
# regDate = scrapy.Field()
# compName = scrapy.Field()
# category = scrapy.Field()
# dateComm = scrapy.Field()
# address = scrapy.Field()
# contactNumber = scrapy.Field()
# emailId = scrapy.Field()
# websiteUrl = scrapy.Field()
# dirName = scrapy.Field()
# fatherName = scrapy.Field()
# managerName = scrapy.Field()
# manFather = scrapy.Field()
# busNature = scrapy.Field()
# maleWorkers = scrapy.Field()
# femaleWorkers = scrapy.Field()
# youngWorkers = scrapy.Field()
# totalWorkers = scrapy.Field()
# familyMembers = scrapy.Field()
# confWorkers = scrapy.Field()
# certNumber = scrapy.Field()
# certDate = scrapy.Field()

def get_urls():
	urls_start = []
	for urls in coll.distinct("url"):
		if urls.strip().startswith("./r_estdet.asp"):
			urls_start.append(base_url + urls.strip().split("./")[1])
		elif urls.strip().startswith("http://www.labour.delhigovt.nic.in/ser/r_estdet.asp"):
			urls_start.append(urls.strip())	
	return urls_start		

# ./r_estdet.asp
base_url = "http://www.labour.delhigovt.nic.in/ser/"

class LabourDeptSpider(BaseSpider):
	"""docstring for LabourDeptSpider"""
	name = "detailsSpider"
	allowed_domains = []
	# def __init__():
	start_urls = get_urls()
	# start_urls = ["http://" + urls.strip() for urls in coll.distinct("url")]	



	def parse(self,response):
		item = LabourdeptItem()
		items = Selector(response).xpath(".//tr")
		try:
			if items[5].xpath(".//td//text()").extract()[0].strip() == 'Address':
				extracted = items[5].xpath(".//td//text()").extract()
				extracted.pop(0)
				addr = ''
				for details in extracted:
					if len(details.strip().split('Contact No:')) > 1 or len(details.strip().split('Fax:')) > 1:
						if len(details.strip().split('Contact No:')) > 1:
							item['contactNumber'] = details.strip().split('Contact No:')[1].split(" ")
						elif len(details.strip().split('Fax:')) > 1 :
							item['faxNumber'] = details.strip().split('Fax:')[1]	
					else:
						addr = addr + details.strip()
				item['address'] = addr	
		except Exception, e:
			log.msg('Address missing',level=log.ERROR)			
		else:	
			item['_id'] = items[0].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['regDate'] = items[1].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['compName'] = items[2].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['category'] = items[3].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['dateComm'] = items[4].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['emailId'] = items[6].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['websiteUrl'] = items[7].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['dirName'] = items[8].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['fatherName'] = items[9].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['managerName'] = items[10].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['manFather'] = items[11].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			item['busNature'] = items[12].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
			try:
				item['maleWorkers'] = int(items[13].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['maleWorkers'] = None
			try:
				item['femaleWorkers'] = int(items[14].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['femaleWorkers'] = None
			try:
				item['youngWorkers'] = int(items[15].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['youngWorkers'] = None	
			try:
				item['totalWorkers'] = int(items[16].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['totalWorkers'] = None	
			try:
				item['familyMembers'] = int(items[17].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['familyMembers'] = None					
			try:
				item['confWorkers'] = int(items[18].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['confWorkers'] = None	
			try:
				item['certNumber'] = int(items[19].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1])
			except ValueError:
				item['certNumber'] = None	
			item['certDate'] = 	items[20].xpath(".//td//text()").extract()[1].strip().encode('utf-8','ignore').split(':')[1]
		return item
		
		
	