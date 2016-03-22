from selenium import webdriver
from selenium.webdriver.support.ui import Select
import pymongo
from twisted.internet.defer import inlineCallbacks,returnValue 
from bs4 import BeautifulSoup
import re
import logging 
driver = webdriver.PhantomJS()
# driver = webdriver.Firefox()

FORMAT = "%(asctime)-15s %(message)s"
LOG_FILENAME = 'init_links.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.DEBUG,
                    format=FORMAT,
                    )

# driver.find_element_by_name("catid")
# select.options
url = "http://www.labour.delhigovt.nic.in/ser/fse05_search.asp"
driver.get(url)
select = Select(driver.find_element_by_name('natid')).options
select2 = Select(driver.find_element_by_name('catid')).options
base_url = "www.labour.delhigovt.nic.in/ser/"
raw_links = re.compile(r'./r_estdet.asp*')

conn = pymongo.MongoClient('localhost',27017)
db = conn['Zoukloans']
coll = db['labourDeptlinks']


# @inlineCallbacks
def get_data(page):
	# with open('init_links.txt','a+') as f:
	for a in page.find_all('a',href=True):
		if re.match(raw_links,a['href']):
			if coll.find_one({"_id":a['href'].split("=")[1]}):
				continue
			else:
				try:
					inp_dict = {}
					inp_dict["_id"] = a['href'].split("=")[1]
					inp_dict["url"] = a['href']
					coll.insert_one(inp_dict)
				except pymongo.errors.DuplicateKeyError as e:
					logging.error(e)
					print e
					pass	
				# f.write(base_url + a['href'].split('./')[1] + '\n')
	# f.close()			

category = []
for option in select2:
	inp_dict = {}
	inp_dict['_id'] = option.get_attribute("value").encode('utf-8','ignore')
	inp_dict['value'] = option.text.encode('utf-8','ignore')
	category.append(inp_dict)

nature_business = []
for option in select:
	inp_dict = {}
	inp_dict['_id'] = option.get_attribute("value").encode('utf-8','ignore')
	inp_dict['value'] = option.text.encode('utf-8','ignore')
	nature_business.append(inp_dict)

category.pop(0)
nature_business.pop(0)

liste = ["19","20","18","21","22","23","244","24","25","26","27","28","29","30","31","7","32","237","33","250","34","35","12","36","37","38","13"]
count = 1
for cats in category:
	for business in nature_business:
		# count += 1
		if cats["_id"] in ["1","2"]:
			continue
		elif cats["_id"] == "3" and count < 207:
			count +=1
			continue
		else:	
			Select(driver.find_element_by_name('natid')).select_by_value(business['_id'])
			Select(driver.find_element_by_name('catid')).select_by_value(cats['_id'])
			driver.find_element_by_name('rrep').submit()
			try:
				alert = driver.switch_to_alert()
				print alert.text()
				alert.accept()
			except:
				print "no alert to accept"
			html_page = BeautifulSoup(driver.page_source,'html.parser')
			get_data(html_page)
			# logging.debug("%s - %s" %(cats["_id"], business["_id"]))
			print "%s %s" %(cats,business)
			driver.get(url)
		# driver.executre_script("window.navigate('fse05_search.asp')")




# Select(driver.find_element_by_name('natid')).select_by_value(nature_business[1]['_id'])
# Select(driver.find_element_by_name('catid')).select_by_value(category[1]['_id'])

# for a in html_page.find_all('a',href=True):
# 	if re.match(raw_links,a['href']):
# 		print a['href']

 # returnValue('True')
	# returnValue()			

# def get_data(driver):
# # @inlineCallbacks	
# 	with open('init_links.txt','a+') as f:
# 		for elems in driver.find_element_by_xpath(".//a[contains('@href','./r_estdet.asp')]"):
# 			f.write(elems.get_attribute('href'))
# 	f.close()
# 	return 		



		# f.write()
# @inlineCallbacks


