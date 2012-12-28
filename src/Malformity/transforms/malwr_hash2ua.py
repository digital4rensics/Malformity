#!/usr/bin/env python

import re
import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash, UserAgent
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
    'dotransform',
]

#@superuser
@configure(
    label='Hash to User Agent - Malwr',
    description='Returns User Agents from HTTP requests in a Malwr.com report for a Hash',
    uuids=[ 'malformity.v1.Malwr_Hash2UA' ],
    inputs=[ ( 'Malwr', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build request
	page = build(request.value)
	
	try:
		table = page.find("div", {"id" : "network_http"}).findNext('table')
		elements = table.findAll("pre")
		for element in elements:
			text = element.text.splitlines()
			for entry in text:
				if re.search('User-Agent:', entry):
					response += UserAgent(entry[12::])
	except:
		return response
					
	return response