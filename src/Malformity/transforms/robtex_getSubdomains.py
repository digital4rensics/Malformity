#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.robtex import build
from canari.maltego.entities import Domain
from canari.maltego.message import UIMessage

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
    label='Get Subdomains [Robtex]',
    description='Returns Domains listed on Robtex for an IP',
    uuids=[ 'malformity.v1.Robtex_getSubdomains' ],
    inputs=[ ( 'Robtex', Domain ) ],
    debug=True
)
def dotransform(request, response):
    page = build(request.value)
    
    doms = []
    if page.find("span", {"id" : "sharedsub"}):
    	section = page.find("span", {"id" : "sharedsub"}).findNext('ul')
    	for entry in section.findAll("li"):
    		response += Domain(entry.text)
    elif page.find("span", {"id" : "sharedsubv"}):
    	section = page.find("span", {"id" : "sharedsubv"}).findNext('ul')
    	for entry in section.findAll("li"):
    		response += Domain(entry.text)	
    else:
    	response += UIMessage('No subdomains in robtex')
    	
    return response