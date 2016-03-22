from selenium import webdriver
import re
import pymongo
import time
import random
def asklaila_data(url,coll):
	driver = webdriver.PhantomJS()
	time.sleep(random.random()*5)
	driver.get(url.strip())
	items = {}
	try:
		items['_id'] = url.strip()
		try:
			items['Name'] = driver.find_element_by_xpath("//span[@itemprop='name']/h1").text
		except Exception,e:
			print e
			pass
		try:
			temp = []
			for numbers in driver.find_elements_by_xpath("//span[@itemprop='telephone']"):
				temp.append(numbers.text.encode('utf-8','ignore'))
			items['contact_details'] = temp
		except Exception, e:
			print e
			pass

		try:
			temp = driver.find_element_by_xpath("//span[@itemprop='streetAddress']").text.encode('utf-8','ignore')
			if isinstance(temp,basestring):
				items['Street'] = temp
		except Exception, e:
			print e
			pass		
		try:
			temp = driver.find_element_by_xpath("//span[@itemprop='addressLocality']").text.encode('utf-8','ignore')
			if isinstance(temp,basestring):
				items['Locality'] = temp
		except Exception, e:
			print e
			pass		
		try:
			temp = driver.find_element_by_xpath("//span[@itemprop='addressRegion']").text.encode('utf-8','ignore')
			if isinstance(temp,basestring):
				items['Region'] = temp
		except Exception, e:
			print e
			pass	
		try:
			temp = driver.find_element_by_xpath("//span[contains(@href,'mailto:')]").text
			if isinstance(temp,basestring):		
				items['email'] = temp
			# print items['email']
		except Exception, e:
			print e
			pass
		coll.insert_one(items)
	except Exception,e:
		print e
		pass
	driver.close()		
			

conn = pymongo.MongoClient('localhost',27017)
db = conn['Zoukloans']
coll = db['AsklailaLinks']
coll2 = db['AskLaila']

for url in coll.distinct('url'):
	if coll2.find_one({'_id': url.strip()}):
		print 'already exist!!'
		pass
	else:	
		print url
		asklaila_data(url,coll2)
	# print url['url']

