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
    label='IP to Domain - pDNS API[VT]',
    description='IP to Domain - VT pDNS data',
    uuids=[ 'malformity.v1.VT_API_IP2Domain' ],
    inputs=[ ('VirusTotal', IPv4Address)],
    debug=True
)

def dotransform(request, response):
    # Report transform progress
    progress(50)
    ip = request.value
    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    
    parameters = {'ip': ip, 'apikey': config['virustotal/apikey']}
    resp = urllib2.urlopen('%s?%s' % (url, urllib.urlencode(parameters))).read()
    response_dict = json.loads(resp)
        
    #Latest detected URLs"
    try:
    	for i in range(0,len(response_dict['resolutions'])):
        	host = response_dict['resolutions'][i]['hostname']
        	host = Domain(host)
        	response += host
    except IOError:
    	response = 'IO Error'
    except KeyError:
    	response = 'Not Found'


    # Update progress
    progress(100)


    # Return response for visualization
    return response