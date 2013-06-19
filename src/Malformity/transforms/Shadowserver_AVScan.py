#!/usr/bin/env python

import sys
import urllib2
import json
from canari.maltego.utils import debug, progress
from canari.maltego.message import Field
from canari.framework import configure #, superuser
from common.entities import Hash

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Ned Moran'
__email__ = 'ned@shadowserver.org'
__status__ = 'Development'

__all__ = [
	'dotransform',
	]

#@superuser
@configure(
	label='AV Scan - Shadowserver',
	description='AV Scan - Shadowserver',
	uuids=[ 'malformity.v1.Shadowserver_AVScan' ],
	inputs=[ ('Shadowserver', Hash)],
	debug=True
)

def dotransform(request, response):
	# Report transform progress
	progress(50)
	hash = request.value
	total=""

	try:
		e = Hash(hash)
		text = ''
		resp = urllib2.urlopen('https://innocuous.shadowserver.org/api/?query=' + hash).read()
		start_results = resp.find("{")
		end_results = resp.find("}")
		av_results = resp[start_results+1:end_results].replace('"','')	
		text += av_results + ','
		e += Field('AV Name', text, displayname='AV Name')
		response += e 
	except IOError:
		print 'IO Error'

	# Update progress
	progress(100)

	# Return response for visualization
	return response