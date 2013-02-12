#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, AS
from canari.maltego.message import Label
from common.isc import buildas

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
    label='AS Report - ISC',
    description='Returns tracked IPs from ISC AS reports',
    uuids=[ 'malformity.v1.ISC_ASReport' ],
    inputs=[ ( 'ISC', AS ) ],
    debug=True
)

def dotransform(request, response):
	#Build Request
	page = buildas(request.value)

	try:		
		tables = page.find('table').findNext('table')
		for entry in tables.findAll('a'):
			ip = entry.text
			rpts = entry.findNext('td')
			trgts = rpts.findNext('td')
			first = trgts.findNext('td')
			last = first.findNext('td')
			
			temp = IPv4Address(ip)
			temp += Label('Reports', rpts.text)
			temp += Label('Targets', trgts.text)
			temp.linklabel = first.text + ' - ' + last.text

		
			response += temp
	except:
		return response
		
	return response