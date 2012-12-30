#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import Field, MaltegoException
from canari.maltego.entities import Phrase
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
    label='Filename Search - ViCheck',
    description='Returns Hashes from a ViCheck Phrase search and sets the filename',
    uuids=[ 'malformity.v1.ViCheck_FileSearch' ],
    inputs=[ ( 'ViCheck', Phrase ) ],
    debug=True
)

def dotransform(request, response):
    #Build the request
    type = 'name'
    page = build(request.value, type)
    
    try:
    	list = page.findAll(text='MD5:')
    except:
       	raise MaltegoException('No DNS Queries')
    
    for item in list:
    	if item != 'none':
    		md5 = Hash(item.next.next)
    		name = item.previous.previous.previous
    		md5 += Field('Filename', name)
    		response += md5
    
    return response