#!/usr/bin/env python

import mechanize
import re
from BeautifulSoup import BeautifulSoup
from canari.maltego.entities import IPv4Address
from common.entities import Hash
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.threatexpert import build

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
    label='Hash to IP - ThreatExpert',
    description='Returns an IP from an existing ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2IP' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)

def dotransform(request, response):
	# Build the request
	page = build(request.value)
	
	# Search the page to extract all IP addresses present
	try:
		for element in page.findAll(text=re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")):
			response += IPv4Address(element)
	except:
		pass
			
	return response