#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.framework import configure
from canari.maltego.message import MaltegoException

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
	'build',
]

def build(data, type):
	#Build Request based on type
	if type == 'hash':
		url = 'https://vicheck.ca/md5query.php?hash=' + data
	elif type == 'mutex':
		url = 'https://vicheck.ca/searchsb.php?mutex=' + data
	elif type == 'network':
		url = 'https://www.vicheck.ca/searchsb.php?server=' + data
	elif type == 'name':
		url = 'https://www.vicheck.ca/searchsb.php?filename=' + data
	else:
		raise MaltegoException("No type given")
	
	browser = mechanize.Browser()
	
	#Retrieve page and create BS entity
	try:
		report = browser.open(url)
		html = report.read()
		page = BeautifulSoup(html)
	except:
		raise MaltegoException("Report Not Found.")
		
	return page