#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from common.entities import Hash
from canari.maltego.entities import Phrase
from common.vt import build
import re

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
    label='Hash to Compile Time - VirusTotal',
    description='Returns compile time of a hash from a VirusTotal report',
    uuids=[ 'malformity.v1.VT_Hash2Timestamp' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
    page = build(request.value)
    try:
	    comptime = page.find(text=re.compile('timedatestamp.....: '))[34:51]
    except:
    	raise MaltegoException('Could not find Compile Time')
    	
    response += Phrase(comptime)
    	    
    return response
