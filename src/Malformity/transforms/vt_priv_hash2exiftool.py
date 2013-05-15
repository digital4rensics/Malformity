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
    label='Hash to ExifTool - VirusTotal',
    description='Returns ExifTool details from a report on VT',
    uuids=[ 'malformity.v1.VT_Priv_Hash2ExifTool' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
	data = getreport(request.value)
	
	try:
		try:
			exif = data['additional_info']['exiftool']
		except:
			#no exif data
			pass
		try:	
			prod = exif['ProductName']
			response += Phrase(prod)
		except:
			#no Product Name
			pass
		try:
			lang = exif['LanguageCode']
			response += Phrase(lang)
		except:
			#no language code
			pass
		try:
			char = exif['CharacterSet']
			response += Phrase(char)
		except:
			#no character set
			pass
		try:
			orig = exif['OriginalFilename']
			response += Filename(orig)
		except:
			#no original name
			pass
		try:
			time = exif['Timestamp']
			response += Phrase(time)
		except:
			#no timestamp
			pass
		try:
			intern = exif['InternalName']
			response += Phrase(intern)
		except:
			#no internal name
			pass
		try:
			type = exif['FileType']
			response += Phrase(type)
		except:
			#no filetype
			pass
		try:
			desc = exif['FileDescription']
			response += Phrase(desc)
		except:
			#no file description
			pass
		try:
			copy = exif['LegalCopyright']
			response += Phrase(copy)
		except:
			#no copyright data
			pass
		try:
			entry = exif['EntryPoint']
			response += Phrase(entry)
		except:
			#no entry point
			pass
		try:
			ver1 = exif['FileVersionNumber']
			response += Phrase(ver1)
		except:
			#no File Version Number
			pass
		try:
			ver2 = exif['ProductVersion']
			response += Phrase(ver2)
		except:
			#no Product Version
			pass
	except:
		response += UIMessage(data['verbose_msg'])
		
	return response