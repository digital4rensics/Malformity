#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure
from common.entities import Hash, Filename
from canari.maltego.entities import Phrase
from canari.maltego.message import UIMessage
from common.vt import getreport

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
    label='Hash to PE Signature - VirusTotal [Private]',
    description='Returns SigCheck details from a PESig section of a report on VT',
    uuids=[ 'malformity.v1.VT_Priv_Hash2PESig' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
	data = getreport(request.value)
	
	try:
		try:
			addinfo = data['additional_info']
		except:
			#no additional info
			pass
		try:	
			pub = addinfo['sigcheck']['publisher']
			response += Phrase(pub)
		except:
			#no dns data
			pass
		try:
			prod = addinfo['sigcheck']['product']
			response += Phrase(prod)
		except:
			#no product data
			pass
		try:
			desc = addinfo['sigcheck']['description']
			response += Phrase(desc)
		except:
			#no description data
			pass
		try:
			orig = addinfo['sigcheck']['original name']
			response += Filename(orig)
		except:
			#no original name
			pass
		try:
			sign = addinfo['sigcheck']['signers']
			response += Phrase(sign)
		except:
			#no signers
			pass
		try:
			intern = addinfo['sigcheck']['internal name']
			response += Phrase(intern)
		except:
			#no internal name
			pass
	except:
		response += UIMessage(data['verbose_msg'])
		
	return response