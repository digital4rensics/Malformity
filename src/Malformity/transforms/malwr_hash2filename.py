#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash, Filename
from common.malwr import build

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
    label='Hash to Filename - Malwr',
    description='Returns reported Filename Malwr.com report for a Hash',
    uuids=[ 'malformity.v1.Malwr_Hash2Filename' ],
    inputs=[ ( 'Malwr', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build Request
	page = build(request.value)

	#Find the dropped files section, and parse MD5 hashes
	try:
		procs = page.find(text='File name').findNext('td')
		name = procs.text
		response += Filename(name)
	except:
		pass
		
	return response