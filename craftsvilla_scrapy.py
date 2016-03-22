from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pymongo

class Craftsvilla():
	"""docstring for Craftsvilla"""
	def __init__(self):
		
		

# driver = webdriver.Firefox()
driver = webdriver.PhantomJS()
url = "http://www.craftsvilla.com/"
driver.get(url)
list_urls = []
for elems in driver.find_elements_by_class_name("row")[1].find_elements_by_xpath(".//li//a"):
	list_urls.append(elems.get_attribute("href"))

print list_urls		

driver.quit()