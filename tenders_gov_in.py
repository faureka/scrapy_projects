from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymongo

final_data = []
driver = webdriver.PhantomJS()
driver.get("http://tenders.gov.in/innerpage.asp?choice=bd0")

corp = []
open_tender_links = []

select = Select(driver.find_element_by_name("org"))
for options in select.options:
	corp.append(options.text)
driver.close()

def callback_func(driver):
	if str(driver.current_url) != "http://tenders.gov.in/innerpage.asp?choice=bd1":
		return driver.find_elements_by_xpath(".//td[contains('@href','innerpage.asp')]")


for comps in corp:
	driver = webdriver.PhantomJS()
	driver.get("http://tenders.gov.in/innerpage.asp?choice=bd0")
	d = driver.find_element_by_name("org")
	d.send_keys(comps)
	driver.find_element_by_name("submit").click()
	# print driver.current_url
	cont = True
	
	while cont:
		if driver.execute_script("return document.readyState;") == "complete":
			cont = False
		print "jvdfvj"
		time.sleep(2)
			
	links_xpath = driver.find_elements_by_xpath(".//a[contains(@href,'innerpage.asp?choice=bd2')]")
	# print links_xpath
	# print len(links_xpath)
	for elems in links_xpath:
		open_tender_links.append(str(elems.get_attribute("href")))
	# print open_tender_links
	driver.close()	
# print open_tender_links

with open("tenders_links.txt","a+") as f:
	for links in open_tender_links:
		f.write(links + "\n")
	f.close()

connection = pymongo.MongoClient("localhost",27017)
db = connection["Zoukloans"]
collection = db["tenders_gov_in"]
count = 0

with open("tenders_links.txt","r+") as f:
	for links in f.readlines():
		count +=1
		time.sleep(2)
		data = {}
		driver = webdriver.PhantomJS()
		driver.get(links)
		dom_table = driver.find_elements_by_class_name("TabBrdLess")[-1].\
		find_element_by_name("displayform").\
		find_elements_by_tag_name("tr")
		print len(dom_table)
		# print dom_table[0].text
		for elems in dom_table:
			elem = elems.find_elements_by_tag_name("td")
			if len(elem) > 1:
				# print str(elem[0].text) , str(elem[1].text)
				data[elem[0].text.encode('utf-8').replace(".","")] =  elem[1].text.encode('utf-8')
		try:
			collection.insert(data)
			print "data inserted" 
			print "urls scraped %d" %count 
			# print data
		except Exception,e:
			print e
			# print "data not present"	
		final_data.append(data)
		driver.quit()

print corp	