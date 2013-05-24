#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, AS

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

#@superuser
@configure(
    label='IPv4Address to AS [Malc0de result]',
    description='Run this to extract AS from HashSearch result entities',
    uuids=[ 'malformity.v1.Malc0de_IP2AS' ],
    inputs=[ ( 'Malc0de', IPv4Address ) ],
    debug=True
)
def dotransform(request, response):
    if request.fields['AS']:
    	response += AS(request.fields['AS'])
    return response