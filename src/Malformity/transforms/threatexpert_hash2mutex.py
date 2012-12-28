#!/usr/bin/env python

import mechanize
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash
from canari.maltego.entities import Phrase
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
    'dotransform',
]

#@superuser
@configure(
    label='Hash to Mutex - ThreatExpert',
    description='Returns a Mutex from an existing ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2Mutex' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build the request
	page = build(request.value)
	
	try:
		try:
			# Searching for the string that indicates a single mutex was created
			single = page.find(text='To mark the presence in the system, the following Mutex object was created:').findNext('ul').li.text
		except:
			single = None
		try:
			# Searching for the string that indicates multiple mutexes were created
			multiple = page.find(text='To mark the presence in the system, the following Mutex objects were created:').findNext('ul')
		except:
			multiple = None	
			
		# If a single mutex was found
		if single is not None:
			response += Phrase(single)
			# Account for the instance in which a dropped file may have had additional mutexes
			if multiple is not None:
				for mutex in multiple.findAll('li'):
					current = mutex.text
					response += Phrase(current)
		# If multiple mutexes were found
		elif multiple is not None:
			for mutex in multiple.findAll('li'):
					current = mutex.text
					response += Phrase(current)
			return response
		else:
			pass
	
	except:
		pass
	
	return response