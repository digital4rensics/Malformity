#!/usr/bin/env python

from json import loads
from canari.maltego.utils import debug, progress
from canari.framework import configure 
from canari.maltego.entities import IPv4Address, Domain
#from sploitego.framework import configure
#from sploitego.maltego.message import Label, UIMessage
#from sploitego.maltego.utils import debug
from urllib import urlopen, urlencode
from common.entities import Malware, Hash

__author__ = 'Kyle Maxwell'
__copyright__ = 'Copyright 2012, Kyle Maxwell'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Kyle Maxwell'
__email__ = '@kylemaxwell'
__status__ = 'Development'

__all__ = [
    'dotransform',
]


@configure(
    label="To malware name [VT]",
    description="Returns names of malware associated with a particular hash",
    uuids=['malformity.v1.VT_Hash2Name'],
    inputs=[('VirusTotal', Hash)]
)
def dotransform(request, response):

    debug('VT API key %s\n' % request.value)

    r = urlopen(
        "https://www.virustotal.com/vtapi/v2/file/report",
        urlencode({
            "resource": request.value,
            "apikey": config['virustotal/apikey']
        })
    )

    if r.code == 200:
        d = loads(r.read())
        debug('VT output: %s\n' % d)

        # If it's not a clean file, tell Maltego the names of the malware
        if d['response_code'] == 1:
            for engine in d['scans'].iteritems():
                if engine[1]['detected']:
                    e = Malware(engine[1]['result'])
                    e += Label("VirusTotal Report", d['permalink'])
                    response += e

        response += UIMessage(d['verbose_msg'])

    return response
