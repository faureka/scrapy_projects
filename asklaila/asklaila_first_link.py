from selenium import webdriver
import re
import pymongo
driver = webdriver.PhantomJS()

def linkextractor(driver,coll):
	print driver.current_url
	for i in xrange(0,200,10):
		if i == 0:
			urls = set()
			elems = driver.find_elements_by_xpath("//a[starts-with(@href,'http://www.asklaila.com/listing')]")
			for elem in elems:
				# print elem.get_attribute('href')
				coll.insert_one({"url": elem.get_attribute('href').encode('utf-8','ignore')})
				urls.add(elem.get_attribute('href'))
		else:
			# url = "http://www.asklaila.com/search/Delhi-NCR/-/Labs%20%26%20Diagnostic%20Centre/" + str(i) + "?searchNearby=false"
			# driver.get(url)
			urls = set()
			elems = driver.find_elements_by_xpath("//a[starts-with(@href,'http://www.asklaila.com/listing')]")
			for elem in elems:
				# print elem.get_attribute('href')
				coll.insert_one({"url": elem.get_attribute('href').encode('utf-8','ignore')})
				urls.add(elem.get_attribute('href'))
	return "Pass"					
# driver = webdriver.Firefox()
conn = pymongo.MongoClient('localhost',27017)
db = conn['Zoukloans']
coll = db['AsklailaLinks']

count = 0
with open('/Users/faizan/Documents/untitled folder/scrapy/asklaila/asklaila_links_first.txt','r+') as f:
	with open('/Users/faizan/Documents/untitled folder/scrapy/asklaila/asklaila_links_second.txt','w+') as f_write:    
	    for url in f.readlines():
			driver.get(url.strip())
			count +=1
			print "line count :%d" %(count)
			print linkextractor(driver,coll)
	
driver.quit()


# init_url = "http://www.asklaila.com/Delhi-NCR-City-Guide/cg2"
# driver.get(init_url)
# urls_links  =  driver.find_elements_by_xpath("//a[contains(@href,'www.asklaila.com/search/')]")
# urls = set()
# for url in urls_links:
# 	temp = url.get_attribute('href').encode('utf-8','ignore')
# 	print temp
# 	urls.add(temp)


