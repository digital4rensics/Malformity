#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.malc0de import build
from common.entities import Hash
from canari.maltego.entities import IPv4Address, URL, AS, Phrase

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


#@superuser
@configure(
    label='IP to Hash, URL [Malc0de]',
    description='Returns Hash and URL entities from search matches on Malc0de',
    uuids=[ 'malformity.v1.Malc0de_IPSearch' ],
    inputs=[ ( 'Malc0de', IPv4Address ) ],
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
    		
    		e = URL(temp[1])
    		e.url = temp[1]
    		response += e
    		response += AS(temp[4])
    		response += Phrase(temp[0])
    		response += Hash(temp[6])
			
    return response
