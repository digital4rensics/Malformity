#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.malc0de import build
from common.entities import Hash
from canari.maltego.entities import IPv4Address
from canari.maltego.message import Field

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.2'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'dotransform'
]

#@superuser
@configure(
    label='Hash to URL [Malc0de]',
    description='Returns IP and URL entities from search matches on Malc0de',
    uuids=[ 'malformity.v1.Malc0de_HashSearch' ],
    inputs=[ ( 'Malc0de', Hash ) ],
    debug=True
)

def dotransform(request, response):
    page = build(request.value)
    
    if page.find('span', {'id' : 'error'}):
    	# No Matches in Malc0de
    	return response
    else:
    	for hit in page.findAll('tr', {'class' : 'class1'}):
    		temp = []
    		for column in hit.findAll('td'):
    			temp.append(column.text)
    		
    		e = IPv4Address(temp[2])
    		e += Field('URL', temp[1], displayname='URL')
    		e += Field('AS', temp[4], displayname='AS Number')
    		e += Field('Date', temp[0], displayname='Date')
    		response += e

    return response