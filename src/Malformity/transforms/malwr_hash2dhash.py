#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
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
    label='Hash to Dropped File Hash - Malwr',
    description='Returns MD5 hashes of all dropped files from a Malwr.com report for a Hash',
    uuids=[ 'malformity.v1.Malwr_Hash2dHash' ],
    inputs=[ ( 'Malwr', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build Request
	page = build(request.value)

	#Find the dropped files section, and parse MD5 hashes
	try:
		procs = page.find("div", {"id" : "dropped_files"}).findAll('tr')
		for element in procs:
			if element.findNext('td').text == "MD5:":
				response += Hash(element.text[4::])
	except:
		return response
		
	return response