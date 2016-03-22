from selenium import webdriver
import pymongo
import random
import time
# reject_list = ['Sr No.','Name','Sector','Institution','Abstract/ Full Version']

conn = pymongo.MongoClient('localhost',27017)
db = conn['Zoukloans']
coll = db['msmePolicies']

driver = webdriver.Firefox()
driver.get('http://www.clusterobservatory.in/schemes.php')
driver.execute_script('search();')

def parse_items(items,coll):
	for item in items:
		try:
			imp_dict = {}
			imp_dict['_id'] = int(item[0].text)
			imp_dict['Name'] = item[1].text.encode('utf-8','ignore')
			imp_dict['Sector'] = item[2].text.encode('utf-8','ignore')
			imp_dict['Institution'] = item[3].text.encode('utf-8','ignore')
			imp_dict['links'] = item[4].find_element_by_xpath('.//a').get_attribute('href')
			coll.insert_one(imp_dict)
			print imp_dict
		except Exception, e:
			print e
			pass
	return	


for i in xrange(1,8):
	istr = str(i)
	func_call = "displayRecords('30','%s');" %istr
	print func_call
	driver.execute_script(func_call) 
	srnos = driver.find_elements_by_class_name('srno')[1:]
	names = driver.find_elements_by_class_name('name')[1:]
	sectors = driver.find_elements_by_class_name('sector')[1:]
	institutions = driver.find_elements_by_class_name('author')[1:]
	pdf_links = driver.find_elements_by_class_name('download')[1:]
	try:
		if len(srnos) == len(names) == len(sectors) == len(institutions) == len(pdf_links):
			liste = zip(srnos,names,sectors,institutions,pdf_links)
			for item in liste:
				imp_dict = {}
				imp_dict['_id'] = int(item[0].text)
				imp_dict['Name'] = item[1].text.encode('utf-8','ignore')
				imp_dict['Sector'] = item[2].text.encode('utf-8','ignore')
				imp_dict['Institution'] = item[3].text.encode('utf-8','ignore')
				imp_dict['links'] = item[4].get_attribute('href')
				coll.insert_one(imp_dict)
		else:
			print "unequal size"	
		print "Done Pages: %d" %i
		time.sleep(random.random()*5)
	except Exception, e:
		raise e	


		

