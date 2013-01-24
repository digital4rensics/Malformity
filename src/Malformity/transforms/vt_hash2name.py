#!/usr/bin/env python

from canari.maltego.utils import debug, progress
from canari.framework import configure #, superuser
from canari.config import config
from common.entities import Hash
from canari.maltego.entities import Phrase
from canari.maltego.message import Label, UIMessage
from urllib import urlopen, urlencode
from json import loads


__author__ = 'Kyle Maxwell'
__copyright__ = 'Copyright 2012, Kyle Maxwell'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Kyle Maxwell'
__email__ = '@kylemaxwell'
__status__ = 'Development'

__all__ = [
    'dotransform'
]


@configure(
    label="To malware name [VT]",
    description="Returns names of malware associated with a particular hash",
    uuids=['malformity.v1.VT_Hash2Name'],
    inputs=[('VirusTotal', Hash)],
    debug=False
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
                    e = Phrase(engine[1]['result'])
                    e += Label("VirusTotal Report", d['permalink'])
                    response += e

        response += UIMessage(d['verbose_msg'])

    return response

