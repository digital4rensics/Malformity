#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash
from canari.maltego.entities import AS

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
    label='Hash to AS [Malc0de result]',
    description='Run this to extract AS from IPSearch result entities',
    uuids=[ 'malformity.v1.Malc0de_Hash2AS' ],
    inputs=[ ( 'Malc0de', Hash ) ],
    debug=True
)
def dotransform(request, response):
    if request.fields['AS']:
    	response += AS(request.fields['AS'])
    return response