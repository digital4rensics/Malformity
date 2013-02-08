#!/usr/bin/env python

import json
import datetime
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import Domain
from common.pdns import query

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
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
	label='Wildcard Domain Search - pDNS',
	description='The transform will return domains retrieved from a wildcard rrset search',
	uuids=[ 'malformity.v1.pDNS_WildcardSearch' ],
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
#			for item in data['rrname']: 
			e = Domain(data['rrname'].rstrip('.'))
			e.linklabel = fnice + ' - ' + lnice
			response += e
				
	return response