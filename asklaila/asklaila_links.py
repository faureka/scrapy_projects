from selenium import webdriver
import re
import pymongo
# driver = webdriver.PhantomJS()
driver = webdriver.Firefox()
# init_url = "http://www.asklaila.com/search/Delhi-NCR/-/Labs%20%26%20Diagnostic%20Centre/?searchNearby=false"
# # reject_list = ['https://www.facebook.com/sharer.php?','https://plus.google.com/share?','https://twitter.com/intent/tweet']


# for i in xrange(0,200,10):
# 	if i == 0:
# 		driver.get(init_url)
# 		urls = set()
# 		elems = driver.find_elements_by_xpath("//a[starts-with(@href,'http://www.asklaila.com/listing')]")
# 		for elem in elems:
# 			# print elem.get_attribute('href')
# 			urls.add(elem.get_attribute('href'))
# 	else:
# 		url = "http://www.asklaila.com/search/Delhi-NCR/-/Labs%20%26%20Diagnostic%20Centre/" + str(i) + "?searchNearby=false"
# 		driver.get(url)
# 		urls = set()
# 		elems = driver.find_elements_by_xpath("//a[starts-with(@href,'http://www.asklaila.com/listing')]")
# 		for elem in elems:
# 			# print elem.get_attribute('href')
# 			urls.add(elem.get_attribute('href'))		

# driver.quit()

conn = pymongo.MongoClient('localhost',27017)
db = conn['Zoukloans']
coll = db['AskLaila']
with open('links.txt','r+') as f_links:
	for url in f_links.readlines():
		driver.get(url.strip())
		# driver.get(test_url)
		items = {}
		try:
			if coll.find_one({'_id': url.strip()}):
				print 'already exist!!'
				pass
			else:	
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
			continue
			
driver.quit()		



# from selenium import webdriver
# import re
# import pymongo

# # urls = list(urls)
# # test_url = "http://www.asklaila.com/listing/Delhi-NCR/Dwarka+Sector+5/Dhanwantri+Labs+%26+Diagnostic+Centre/1PSttelF/"
# 		for url in urls:
# driver = webdriver.Firefox()
# test_url = "http://www.asklaila.com/listing/Delhi-NCR/Dwarka+Sector+5/Dhanwantri+Labs+%26+Diagnostic+Centre/1PSttelF/"
# driver.get(test_url)
# items = {}
# print driver.find_element_by_xpath("//span[@itemprop='name']/h1").text

