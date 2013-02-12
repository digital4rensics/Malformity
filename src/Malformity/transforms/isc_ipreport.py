#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, Phrase, Service
from common.isc import build

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
    label='IP Report - ISC',
    description='Returns targeted ports from ISC IP reports',
    uuids=[ 'malformity.v1.ISC_IPReport' ],
    inputs=[ ( 'ISC', IPv4Address ) ],
    debug=True
)

def dotransform(request, response):
	#Build Request
	page = build(request.value)

	try:
		comment = page.find('div', {'class' : 'altborder'})
		response += Phrase(comment.text)
		
		prts = page.findAll('td', text = "-NA-")
		for entry in prts:
			prt = entry.findNext('td')
			prot = prt.findNext('td')
			
			if prot.text != "":
				msg = "Noted targeting port " + prt.text + ", using protocol " + prot.text
			else:
				msg = "Noted targeting port " + prt.text
			
			response += Service(msg)
	except:
		return response
		
	return response