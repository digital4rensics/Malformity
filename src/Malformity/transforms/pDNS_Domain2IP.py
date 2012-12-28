#!/usr/bin/env python

import json
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, Domain
from common.pdns import query

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
__credits__ = ['ISC for the original pDNS python script']

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
	label='Domain to IPs - pDNS',
	description='The transform will take a domain and return IP addresses based on pDNS records',
	uuids=[ 'malformity.v1.pDNS_Domain2IP' ],
	inputs=[ ( 'pDNS', Domain ) ],
	debug=True
)

def dotransform(request, response):
	domain = request.value
	results = query('-r', domain, 0, 'n')

	for result in results:
		data = json.loads(result)
		if data.has_key('rdata'):
			for item in data['rdata']:
				response += IPv4Address(item)
			
	return response