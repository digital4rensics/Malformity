#!/usr/bin/env python

import re
import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.threatexpert import build
from common.entities import Hash

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
    label='Hash to Dropped File Hash - ThreatExpert',
    description='Returns MD5 hashes of all dropped files from a ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2dHash' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build the request
	page = build(request.value)

	#Locate the dropped files section of the report
	try:
		dfiles = page.find(text='The following files were created in the system:').findNext('table')
	except:
		dfiles = None
		pass
	
	if dfiles is not None:
		#Find the appropriate cell and extract the MD5 hash
		for file in dfiles.findAll("td", {"class" : "cell_1"}):
			text = file.text.splitlines()
			for entry in text:
				if re.search('MD5:', entry):
					response += Hash(entry[7:39])
	else:
		return response
		
	return response