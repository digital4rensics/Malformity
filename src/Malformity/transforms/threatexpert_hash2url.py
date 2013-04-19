#!/usr/bin/env python

import re
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.threatexpert import build
from common.entities import Hash
from canari.maltego.entities import URL

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]

#@superuser
@configure(
    label='Hash to URL - ThreatExpert',
    description='Returns URLs from a ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2URL' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build the request
	page = build(request.value)

	#Locate the URL files section of the report
	try:
		urls = page.find(text='The data identified by the following URLs was then requested from the remote web server:').findNext('ul')
	except:
		urls = None
		pass
	try:
		url = page.find(text='The data identified by the following URL was then requested from the remote web server:').findNext('ul')
	except:
		url = None
	
	if urls is not None:
		#Find the appropriate cell and extract the MD5 hash
		for file in urls.findAll("li"):
			text = file.text
			e = URL(text)
			e.url = text
			response += e
	elif url is not None:
		for file in url.findAll("li"):
			text = file.text
			e = URL(text)
			e.url = text
			response += e
	else:
		return response
		
	return response