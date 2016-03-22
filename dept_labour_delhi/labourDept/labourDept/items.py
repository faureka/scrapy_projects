# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LabourdeptItem(scrapy.Item):
	compName = scrapy.Field()
	# regNumber = scrapy.Field()
	regDate = scrapy.Field()
	category = scrapy.Field()
	dateComm = scrapy.Field()
	address = scrapy.Field()
	contactNumber = scrapy.Field()
	emailId = scrapy.Field()
	websiteUrl = scrapy.Field()
	dirName = scrapy.Field()
	fatherName = scrapy.Field()
	managerName = scrapy.Field()
	manFather = scrapy.Field()
	busNature = scrapy.Field()
	maleWorkers = scrapy.Field()
	femaleWorkers = scrapy.Field()
	youngWorkers = scrapy.Field()
	totalWorkers = scrapy.Field()
	familyMembers = scrapy.Field()
	confWorkers = scrapy.Field()
	certNumber = scrapy.Field()
	certDate = scrapy.Field()
	faxNumber = scrapy.Field()
	_id = scrapy.Field()

    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
