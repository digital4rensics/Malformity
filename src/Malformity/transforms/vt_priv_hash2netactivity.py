#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure
from common.entities import Hash, UserAgent, HTTPRequest
from canari.maltego.entities import Domain, IPv4Address, URL, Port
from canari.maltego.message import UIMessage
from common.vt import getbehavior

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
    label='Hash to Network Information - VirusTotal',
    description='Returns network details from a behavioural report on VT',
    uuids=[ 'malformity.v1.VT_Priv_Hash2NetActivity' ],
    inputs=[ ( 'VirusTotal', Hash ) ],
    debug=True
)

def dotransform(request, response):
	data = getbehavior(request.value)

	try:
		try:
			network = data['network']
		except:
			#no network data
			pass
		try:	
			for result in network['dns']:
				dom = result['hostname']
				ip = result['ip']
				response += Domain(dom)
				response += IPv4Address['ip']
		except:
			#no dns data
			pass
		try:
			for request in network['http']:
				uri = URL(request['uri'])
				uri.url = request['uri']
				
				ua = UserAgent(request['user-agent'])
				req = HTTPRequest(request['data'])
				port = Port(request['port'])
				
				response += uri
				response += ua
				response += req
				response += port
		except:
			#no http data
			pass
		try:
			for entry in network['tcp']:
				e = entry['dst']
				if e.startswith('10.'):
					pass
				else:
					conn = IPv4Address(e)
					response += conn
		except:
			#no tcp data
			pass
	except:
		response += UIMessage(data['verbose_msg'])
		
	return response