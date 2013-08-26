#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.robtex import build
from canari.maltego.entities import IPv4Address, Domain

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
    label='IP to Domains [Robtex]',
    description='Returns Domains listed on Robtex for an IP',
    uuids=[ 'malformity.v1.Robtex_IP2Domain' ],
    inputs=[ ( 'Robtex', IPv4Address ) ],
    debug=True
)
def dotransform(request, response):
    page = build(request.value)
    
    doms = []
    section = page.find("span", {"id" : "sharedha"}).findNext('ul')
    for entry in section.findAll("li"):
    	response += Domain(entry.text)
    	
    return response