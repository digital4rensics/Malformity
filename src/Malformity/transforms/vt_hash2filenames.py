#!/usr/bin/env python

import re
from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from common.entities import Hash, Filename
from common.vt import build

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'dotransform',
]

@configure(
    label='Hash to Filenames - VirusTotal',
    description='Returns submitted filenames for a hash from a VirusTotal report',
    uuids=[ 'malformity.v1.VT_Hash2Filenames' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
	page = build(request.value)
	try:    
		results = page.findAll('td', {"class" : "field-key"})
		for entry in results:
			text = entry.text
			if re.search('File names', text):
				lines = ''.join(entry.next.next.next.findAll(text=True))
				for line in lines.split():
					response += Filename(line)
	except:
		raise MaltegoException('Could not find Filenames')

	return response