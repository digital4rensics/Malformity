#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
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
    label='Hash to Dropped Hash - ViCheck',
    description='Returns Dropped Files from a ViCheck report for a hash',
    uuids=[ 'malformity.v1.ViCheck_Hash2dHash' ],
    inputs=[ ( 'ViCheck', Hash ) ],
    debug=True
)

def dotransform(request, response):
	#Build the request
	type = 'hash'
	page = build(request.value, type)

	global count
	global count2
	count = 1

	try:
		list = page.find(text='Dropped File').previous.previous.parent.findAll('p')
	except:
		raise MaltegoException('No Dropped Files')

	for item in list:
		count2 = 1
		if count % 2 == 1:
			split = item.findAll('a')
			for s in split:
				if count2 % 2 == 1:
					pass
				else:
					e = Hash(s.text)
					response += e
				count2+=1
		elif count % 2 == 0:
			pass
		count+=1

	return response