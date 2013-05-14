#!/usr/bin/env python

import json
import mechanize
import requests
from BeautifulSoup import BeautifulSoup
from canari.framework import configure
from canari.config import config
from canari.maltego.message import MaltegoException

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
	'build',
]

def build(hash):
	url = 'http://www.virustotal.com/file/' + hash + '/analysis/'
	
	browser = mechanize.Browser()
	
	# Retrieve the page and construct BS entity if it exists
	try:
		report = browser.open(url)
		html = report.read()
		page = BeautifulSoup(html)
	except:
		raise MaltegoException("Report Not Found.")
		
	return page

privkey = config['virustotal/privkey']
	
def bsearch(term):
	params = {'apikey': privkey, 'query': 'behaviour:'+term}
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/search', params=params, verify=False)
	response_json = response.json()
	
	return response_json
	
def getreport(hash):
	params = {'apikey' : privkey, 'hash' : hash}
	response = requests.get('https://www.virustotal.com/vtapi/v2/file/behaviour', params=params, verify=False)
	response_json = response.json()
	
	return response_json