#!/usr/bin/env python

import json
import datetime
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, Domain, MXRecord, NSRecord
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
		if data.has_key('time_first'):
			first = data['time_first']
			last = data['time_last']
		elif data.has_key('zone_time_first'):
			first = data['zone_time_first']
			last = data['zone_time_last']
			
		fnice = datetime.datetime.fromtimestamp(int(first)).strftime('%m-%d-%Y')
		lnice = datetime.datetime.fromtimestamp(int(last)).strftime('%m-%d-%Y')
		
		if data['rrtype'] == 'A':
			for item in data['rdata']: 
				e = IPv4Address(item)
				e.linklabel = fnice + ' - ' + lnice
				response += e
		elif data['rrtype'] == 'NS':
			for item in data['rdata']:
				e = NSRecord(item)
				e.linklabel = fnice + ' - ' + lnice
				response += e
		elif data['rrtype'] == 'MX':
			for item in data['rdata']:
				e = MXRecord(item)
				e.linklabel = fnice + ' - ' + lnice
				response += e
		elif data['rrtype'] == 'CNAME':
			for item in data['rdata']:
				e = Domain(item.rstrip('.'))
				e.linklabel = fnice + ' - ' + lnice
				response += e
		elif data['rrtype'] == 'TXT':
			pass
		else:
			for item in data['rdata']:
				e = IPv4Address(item)
				e.linklabel = fnice + ' - ' + lnice
				response += e
				
	return response