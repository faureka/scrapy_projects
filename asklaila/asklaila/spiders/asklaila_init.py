from scrapy.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy import Selector
from asklaila.items import AsklailaItem

import pymongo

class asklaila_spider(CrawlSpider):
    name = "asklaila_init"
    allowed_domains = []
    start_urls = list(set([l.strip() for l in open('links.txt').readlines()]))
    
    # rule = Rule(LinkExtractor(allow=(),restrict_xpath('.//a[@class="btnNextPre"]'),callback='parse_item',follow=True)

    def parse(self, response):
        urls = Selector(response).xpath('.//*[@itemscope]')
        print urls.xpath('@itemtype').extract()
	     for property in item.xpath('.//*[@itemprop]'):
	        print property.xpath('@itemprop').extract(),
	        print property.xpath('string(.)').extract()






        print len(urls)
        for url in urls:
            item = AsklailaItem()
            item['name']= 
            item['url']=
            item['telephone']=
            item['adr']=
            return item
