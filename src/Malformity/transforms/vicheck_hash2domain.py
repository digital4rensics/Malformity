#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from canari.maltego.entities import Domain
from common.entities import Hash
from common.vicheck import build

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

@configure(
    label='Hash to Domains - ViCheck',
    description='Returns Domains from a ViCheck report for a hash',
    uuids=[ 'malformity.v1.ViCheck_Hash2Domain' ],
    inputs=[ ( 'ViCheck', Hash ) ],
    debug=True
)

def dotransform(request, response):
    #Build the request
    type = 'hash'
    page = build(request.value, type)
    
    try:
    	list = page.find(text='PCAP Raw DNS Queries').previous.previous.parent.findAll('p')
    except:
    	raise MaltegoException('No DNS Queries')
    
    for item in list:
    	if item.text != 'none':
    		response += Domain(item.text)
    
    return response