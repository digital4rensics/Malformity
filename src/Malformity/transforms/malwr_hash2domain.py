#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import Domain
from common.entities import Hash
from common.malwr import build

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2012, Malformity Project'
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
    label='Hash to Domains - Malwr',
    description='Returns a Domain(s) from a Malwr.com report for a Hash',
    uuids=[ 'malformity.v1.Malwr_Hash2Domain' ],
    inputs=[ ( 'Malwr', Hash ) ],
    debug=True
)
def dotransform(request, response):
    #Build Request
    page = build(request.value)
    	
    #Finds the DNS section and extracts domains
    try:
    	table = page.find("div", {"id" : "network_dns"}).findNext('table')
    	elements = table.findAll("span", {"class" : "mono"})
    	for element in elements:
    		text = element.find(text=True)
    		response += Domain(text)
    except:
    	return response
    
    return response