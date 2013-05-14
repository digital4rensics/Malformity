#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure
from common.entities import Hash
from canari.maltego.entities import IPv4Address
from common.vt import bsearch

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
    label='IP Search - VirusTotal',
    description='Searches VirusTotal for samples based on an IP',
    uuids=[ 'malformity.v1.VT_Priv_IP2Hash' ],
    inputs=[ ( 'VirusTotal', IPv4Address ) ],
    debug=True
)

def dotransform(request, response):
    data = bsearch(request.value)
    try:
    	if data['response_code'] == 1:
    		results = data['hashes']
    		for result in results:
    			response += Hash(result)
    except:
    	print 'Error running transform'	
    
    return response