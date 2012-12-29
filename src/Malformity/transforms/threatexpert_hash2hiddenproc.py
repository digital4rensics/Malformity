#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash, MaliciousProcess
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
    label='Hash to Hidden Process - ThreatExpert',
    description='Returns a list of hidden processes from a ThreatExpert report for a Hash',
    uuids=[ 'malformity.v1.ThreatExpert_Hash2HiddenProc' ],
    inputs=[ ( 'ThreatExpert', Hash ) ],
    debug=True
)
def dotransform(request, response):
    page = build(request.value)
    
    try:
    	dfiles = page.find(text=' from the user:').findNext('table')
    except:
    	dfiles = None
    	pass
    
    if dfiles is not None:
    	for file in dfiles.findAll("td", {"class" : "cell_1"}):
    		text = file.text.splitlines()
    		for entry in text:
    			response += MaliciousProcess(entry)
    
    return response
