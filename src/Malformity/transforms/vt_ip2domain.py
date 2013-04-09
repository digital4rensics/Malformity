#!/usr/bin/env python

import urllib2
from canari.maltego.utils import debug, progress
from BeautifulSoup import BeautifulSoup, NavigableString
from canari.framework import configure #, superuser
from canari.maltego.entities import IPv4Address, Domain

__author__ = 'Marcus'
__copyright__ = 'Copyright 2013, Marcus'
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
    label='IP to Domain - pDNS [VT]',
    description='IP to Domain - VT pDNS data',
    uuids=[ 'malformity.v1.VT_IP2Domain' ],
    inputs=[ ('VirusTotal', IPv4Address)],
    debug=True
)

def dotransform(request, response):
    # Report transform progress
    progress(50)
    ip = request.value
    total=""

    urldom = 'https://www.virustotal.com/en/ip-address/'+ip+'/information/'
    soup = BeautifulSoup(urllib2.urlopen(urldom).read())
    try:
        links = soup.findAll('div', attrs={'class':'enum'})
        for link in links:
            total += str(link)
        total = BeautifulSoup(total)
        for totals in total.findAll('a',href=True):
            totals=totals['href']
            theIP = totals.replace("/en/domain/", "")
            e = theIP.replace("/information/", "")
            e = Domain(e)
            response += e
    except IOError:
        print 'IO Error'


    # Update progress
    progress(100)


    # Return response for visualization
    return response