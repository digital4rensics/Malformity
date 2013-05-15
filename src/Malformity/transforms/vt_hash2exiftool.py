#!/usr/bin/env python

from BeautifulSoup import BeautifulSoup
from canari.maltego.utils import debug, progress
from canari.framework import configure
from canari.maltego.message import MaltegoException
from common.entities import Hash, Filename
from canari.maltego.entities import Phrase
from common.vt import build
import re

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
    label='Hash to ExifTool - VirusTotal',
    description='Returns ExifTool details from a report on VT',
    uuids=[ 'malformity.v1.VT_Hash2ExifTool' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
	page = build(request.value)
	try:    
		results = page.findAll('span', {"class" : "field-key"})
		for entry in results:
			text = entry.text
			if re.search('TimeStamp', text):
				e = entry.next.next.strip()
				response += Phrase(e)
			elif re.search('FileType', text):
				e = entry.next.next.strip()
				response += Phrase(e)
			elif re.search('EntryPoint', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('FileVersionNumber', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('LanguageCode', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('CharacterSet', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('InternalName', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('FileDescription', text):
				e= entry.next.next.strip()
				response += Phrase(e)
			elif re.search('OriginalFilename', text):
				e= entry.next.next.strip()
				response += Filename(e)
			elif re.search('ProductVersionNumber', text):
				e= entry.next.next.strip()
				response += Phrase(e)
	except:
		raise MaltegoException('Could not Exif Information')

	return response