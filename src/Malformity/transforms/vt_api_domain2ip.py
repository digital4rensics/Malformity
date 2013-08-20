#!/usr/bin/env python

import urllib2
import urllib
import json
from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, Domain
from canari.config import config

__author__ = 'Marcus'

# ...
#@superuser
@configure(
    label='Domain to IP - pDNS API[VT]',
    description='Domain to IP - VT pDNS data',
    uuids=[ 'malformity.v1.VT_API_Domain2IP' ],
    inputs=[ ('VirusTotal', Domain)],
    debug=True
)

def dotransform(request, response):
    # Report transform progress
    progress(50)
    domain = request.value
    url = 'https://www.virustotal.com/vtapi/v2/domain/report'
    
    parameters = {'domain': domain, 'apikey': config['virustotal/apikey']}
    resp = urllib2.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(resp)
        
    #Latest detected IPs"
    try:
    	for i in range(0,len(response_dict['resolutions'])):
        	ip = response_dict['resolutions'][i]['ip_address']
        	ip = IPv4Address(ip)
        	response += ip
    except IOError:
    	response = 'IO Error'
    except KeyError:
    	response = 'Not Found'


    # Update progress
    progress(100)


    # Return response for visualization
    return response