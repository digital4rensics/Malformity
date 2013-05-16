#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.framework import configure #, superuser
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

def build(term):
	url = 'http://malc0de.com/database/index.php?&search=' + term
	browser = mechanize.Browser()
	
	#Retrieve page and create BS entity if the page exists
	try:
		report = browser.open(url)
		html = report.read()
		page = BeautifulSoup(html)
	except:
		raise MaltegoException("Report Not Found.")
		
	return page