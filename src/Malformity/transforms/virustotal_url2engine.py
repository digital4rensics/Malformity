#!/usr/bin/env python

from json import loads
from sploitego.config import config
from sploitego.framework import configure
from sploitego.maltego.message import Label
from sploitego.maltego.utils import debug
from urllib import urlopen, urlencode
from common.entities import AntiVirusEngine, Hash

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
    label="To AV Engine [VT]",
    description="Returns names of AV engines that flagged the URL.",
    uuids=['virustotal.v2.MalwareToAntiVirusEngine_VT'],
    inputs=[('VirusTotal', URL)]
)
def dotransform(request, response):

    debug('VT API key %s\n' % config['virustotal/apikey'])

    r = urlopen(
        "https://www.virustotal.com/vtapi/v2/url/report",
        urlencode({
            "resource": request.value,
            "apikey": config['virustotal/apikey']
        })
    )

    if r.code == 200:
        d = loads(r.read())
        debug('VT output: %s\n' % d)

        if d['response_code'] == 1:
            for engine in d['scans'].iteritems():
                if engine[1]['detected']:
                    e = AntiVirusEngine(engine[0])
                    e += Label("VirusTotal Report", d['permalink'])
                    response += e

    return response
