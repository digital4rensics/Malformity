#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from common.entities import Hash, RegistryEntry
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
    label='Hash to Registry - ViCheck',
    description='Returns Registry Items from a ViCheck report for a hash',
    uuids=[ 'malformity.v1.ViCheck_Hash2Registry' ],
    inputs=[ ( 'ViCheck', Hash ) ],
    debug=True
)

def dotransform(request, response):
    #Build the request
    type = 'hash'
    page = build(request.value, type)
    
    try:
    	list = page.find(text='Registry Item Created').previous.previous.parent.findAll('p')
    except:
    	raise MaltegoException('No Registry Items Created')
    
    for item in list:
    	if item.text != 'none':
			response += RegistryEntry(item.text)
    
    return response
