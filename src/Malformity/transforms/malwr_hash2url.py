#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import URL
from common.entities import Hash
from common.malwr import build

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
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
    label='Hash to URL - Malwr',
    description='Returns URLS for HTTP requests from Malwr.com report for a Hash',
    uuids=[ 'malformity.v1.Malwr_Hash2URL' ],
    inputs=[ ( 'Malwr', Hash ) ],
    debug=True
)
def dotransform(request, response):
    #Build request
	page = build(request.value)
	
	#Find the Hosts section and extract IPs	
	try:
		table = page.find("div", {"id" : "network_http"}).findNext('table')
		elements = table.findAll("span", {"class" : "mono"})
		for element in elements:
			text = element.find(text=True)
			response += URL(text)
	except:
		return response
			
	return response