#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from common.entities import Hash, Filename
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
    label='Hash to Filename - ViCheck',
    description='Returns Filename from a ViCheck report for a hash',
    uuids=[ 'malformity.v1.ViCheck_Hash2Filename' ],
    inputs=[ ( 'ViCheck', Hash ) ],
    debug=True
)

def dotransform(request, response):
    #Build the request
    type = 'hash'
    page = build(request.value, type)
    
    try:
    	list = page.find(text='File: ').findNext('b')
    except:
    	raise MaltegoException('No filename')
    
    if list.text != '':
		response += Filename(list.text)
    
    return response
