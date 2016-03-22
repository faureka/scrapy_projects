# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZaubacorpItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    url = scrapy.Field()
    roc_data = scrapy.Field()
    status = scrapy.Field()
    _id = scrapy.Field()
    reg_num = scrapy.Field()
    comp_cat = scrapy.Field()
    comp_sub_cat = scrapy.Field()
    comp_class = scrapy.Field()
    auth_cap = scrapy.Field()
    paid_up_cap = scrapy.Field()
    no_members = scrapy.Field()
    date_incorp = scrapy.Field()
    email = scrapy.Field()
    website = scrapy.Field()
    addr1 = scrapy.Field()
    addr2 = scrapy.Field()
    city = scrapy.Field()
    state = scrapy.Field()
    country = scrapy.Field()
    pin = scrapy.Field()
    activity = scrapy.Field()								#listed or unlisted
    date_AGM = scrapy.Field()
    date_bal_sheet = scrapy.Field()

