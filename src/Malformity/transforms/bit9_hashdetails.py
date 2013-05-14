#!/usr/bin/env python

"""
NOTE: This transform is currently inefficient due to the need to login for every request.
It is suggested that you don't execute the transform on a large group of hashes.
"""

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from common.entities import Hash, Filename
from canari.maltego.entities import Phrase
from common.bit9 import loginSearch

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
    label='Hash Details - Bit9',
    description='Returns details of a hash from Bit9 FileAdvisor',
    uuids=[ 'malformity.v1.Bit9_HashDetails' ],
    inputs=[ ( 'Bit9', Hash ) ],
    debug=True
)

def dotransform(request, response):
	page = loginSearch(request.value)
	results = BeautifulSoup(page)

	try:
		name = results.find('td', {'class' : 'FourColumns_Column_2'}).text
		response += Filename(name)
	
		desc = results.find('td', {'class' : 'FourColumns_Column_4'}).text
		response += Phrase(desc)
	
		result = results.find('td', {'bgcolor' : '#eaffea'}).text
		response += Phrase(result)
	except:
		#no results
		pass
		
	return response