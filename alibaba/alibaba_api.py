import treq
from klein import Klein
from twisted.internet.defer import inlineCallbacks, returnValue
from bs4 import BeautifulSoup
import json
import re
from twisted.python import log
app = Klein()

comp_name_regex = re.compile(r'\b[\w ]+\b')


def clean_text(str,flag='td'):
	if flag == 'td':
		return str.find('td').get_text().replace('-',' ').replace(',','').replace('.','').strip().encode('utf-8','ignore')
	elif flag == 'th':
		return str.find('th').get_text().strip().replace('-',' ').replace(',','').replace('.','').split(':')[0].encode('utf-8','ignore')	


@app.route('/')
def helloworld():
	return "<h>Helloe!!<\h>"

@app.route('/apis/get',methods=['GET',])
@inlineCallbacks
def check_status(request):
	if not request.args.get("cname"):
		pass
		# abort(400)
	# elif not re.match(request.args.get("cname")):	
	else:
		get_url = "http://india.alibaba.com/supplier_list.htm?bizType=&SearchText="
		search_query = request.args.get("cname",[0])[0].strip().replace('.','').replace(',','').upper()
		if re.search(comp_name_regex,search_query):
			search_query = search_query.replace(" ","%20")
			# print search_query
			try:
				response = yield treq.get(get_url+search_query)
				# print response1.status_code
			except Exception,e:
				print e
				log.msg(e,logLevel=logging.DEBUG)
				# response.close()
				abort(404)
			content = yield response.content()	
			soup = BeautifulSoup(content,"html.parser")
			# print soup.find('title').get_text()
			name_comps = soup.find_all("a",{"class":"dot-company"})
			name_url_list = [] 
			for names in name_comps:
				name_url_dict = {}
				name_url_dict['Name'] = names.get("title")
				name_url_dict['href'] = names.get("href")
				name_url_list.append(name_url_dict)
			# response.close()
		returnValue(json.dumps(name_url_list))



@app.route('/apis/get/details',methods=['GET',])
@inlineCallbacks
def get_details(request):
	if not request.args.get('url',[0]):
		# abort(400)
		pass
	else:	
		add_url = "/trustpass_profile.html?certification_type=intl_av"
		try:
			url = request.args.get('url',[0])[0].strip()
			print url
			response = yield treq.get(url.split(".html")[0] + add_url)
		except Exception ,e:
			print e
			log.msg(e,logLevel=logging.DEBUG)
			# response.close()
			# abort(404)
			pass

		# print response2.status_code
		try:
			content = yield response.content()
			soup = BeautifulSoup(content,"html.parser")
			details = soup.find_all("table",{"class":"table"})
			basic_details = details[0].find_all("tr")
			personl_details = details[1].find_all("tr")
			outdict = {}
			for idx,lines in enumerate(basic_details):
				outdict[clean_text(lines,'th')] = clean_text(lines,'td')
				# print clean_text(lines,'td')
			for lines in personl_details:
				outdict[clean_text(lines,'th')] = clean_text(lines,'td')
			returnValue(json.dumps(outdict))
		except KeyError:
				# abort(400)
				pass
	




if __name__ == '__main__':
	app.run(host='localhost',port=5000)
	observer = log.PythonLoggingObserver()
	observer.start()