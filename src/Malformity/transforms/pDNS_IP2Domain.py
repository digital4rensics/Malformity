#!/usr/bin/env python

import json
import datetime
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
	label='IP to Domains - pDNS',
	description='The transform will take an IP address and return domains based on pDNS records',
	uuids=[ 'malformity.v1.pDNS_IP2Domain' ],
	inputs=[ ( 'pDNS', IPv4Address ) ],
	debug=True
)

def dotransform(request, response):
	ip = request.value
	results = query('-i', ip, 0, 'n')

	for result in results:
		data = json.loads(result)
		if data.has_key('rrname'):
			first = data['time_first']
			last = data['time_last']
			fnice = datetime.datetime.fromtimestamp(int(first)).strftime('%m-%d-%Y')
			lnice = datetime.datetime.fromtimestamp(int(last)).strftime('%m-%d-%Y')
			e = Domain(data['rrname'].rstrip('.'))
			e.linklabel = fnice + ' - ' + lnice
			response += e
			
	return response