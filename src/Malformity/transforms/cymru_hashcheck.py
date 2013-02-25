#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.message import Field
from common.entities import Hash
from common.whois import whois
from datetime import datetime

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
    label='Team CYMRU Hashcheck',
    description='Returns targeted ports from ISC IP reports',
    uuids=[ 'malformity.v1.CYMRU_HashCheck' ],
    inputs=[ ( 'CYMRU', Hash ) ],
    debug=True
)

def dotransform(request, response):
	hash = request.value
	host = 'hash.cymru.com'
	
	result = whois(hash, host)
	attribs = result.split()
	
	hsh = attribs[0]
	time = float(attribs[1])
	percent = attribs[2]
	
	if attribs[2] == "NO_DATA":
		e = Hash(hsh)
		e += Field("TeamCymru", "Not Detected", displayname='TeamCymru')
	else:
		e = Hash(hsh)
		e += Field("Cymru Date", datetime.utcfromtimestamp(time), displayname='Cymru Date')
		e += Field("Percent Detected", percent, displayname='Percent Detected')
	
	response += e
						
	return response