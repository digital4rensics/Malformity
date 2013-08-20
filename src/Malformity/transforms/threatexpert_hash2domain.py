#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash
from canari.maltego.entities import Domain
from common.threatexpert import build

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
    label='Hash to Domain - ThreatExpert',
    description='Returns Domains from a ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2Domain' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)
def dotransform(request, response):
    page = build(request.value)
    
    try:
    	single = page.find(text='The following Host Name was requested from a host database:').findNext()
    except:
    	single = None
    	pass
    
    try:
    	single2 = page.find(text='The following Internet Connection was established:').findNext()
    except:
    	single2 = None
    	pass
    	
    try:
    	multi = page.find(text='The following Internet Connections were established:').findNext('table')
    except:
    	multi = None
    	pass

    if single is not None:
    	for dom in single.findAll("li"):
    		text = dom.text
    		response += Domain(text)
    		
    if single2 is not None:
    	dom = single2.findNext('tr').findNext('tr').findNext('td')
    	text = dom.text
    	response += Domain(text)
    		
    if multi is not None:
    	for entry in multi.findAll('tr')[1::]:
    		dom = entry.findNext('td')
    		text = dom.text
    		response += Domain(text)
    
    return response