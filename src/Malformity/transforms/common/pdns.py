#!/usr/bin/env python
# Original script authored by ISC, found here: ftp://ftp.isc.org/isc/nmsg/misc/isc_dnsdb_query.py
# Modifications made by @digital4rensics for use in the Malformity project

import json
import optparse
import os
import sys
import time
import urllib2
from cStringIO import StringIO
from canari.config import config

class DnsdbClient(object):
    def __init__(self, server, apikey):
        self.server = server
        self.apikey = apikey

    def query_rrset(self, oname, rrtype=None, bailiwick=None):
        if bailiwick:
            if not rrtype:
                rrtype = 'ANY'
            path = 'rrset/name/%s/%s/%s' % (oname, rrtype, bailiwick)
        elif rrtype:
            path = 'rrset/name/%s/%s' % (oname, rrtype)
        else:
            path = 'rrset/name/%s' % oname
        return self._query(path)

    def query_rdata_name(self, rdata_name, rrtype=None):
        if rrtype:
            path = 'rdata/name/%s/%s' % (rdata_name, rrtype)
        else:
            path = 'rdata/name/%s' % rdata_name
        return self._query(path)

    def query_rdata_ip(self, rdata_ip):
        path = 'rdata/ip/%s' % rdata_ip.replace('/', ',')
        return self._query(path)

    def _query(self, path):
        res = []
        url = '%s/lookup/%s' % (self.server, path)
        #if limit != 0:
            #url += '?limit=%d' % lim
        req = urllib2.Request(url)
        req.add_header('Accept', 'application/json')
        req.add_header('X-Api-Key', self.apikey)
        try:
            http = urllib2.urlopen(req)
            while True:
                line = http.readline()
                if not line:
                    break
                else:
                	res.append(line)
        except urllib2.HTTPError, e:
            sys.stderr.write(str(e) + '\n')
        return res

def query(opt, sub, lim, sor):
	#global cfg
	#global options
	#global limit
	#limit = lim
	
	DEFAULT_DNSDB_SERVER = 'https://dnsdb-api.isc.org'

	options = None
	"""
	parser = optparse.OptionParser()
	parser.add_option('-r', '--rrset', dest='rrset', type='string',
		help='rrset <ONAME>[/<RRTYPE>[/BAILIWICK]]')
	parser.add_option('-n', '--rdataname', dest='rdata_name', type='string',
		help='rdata name <NAME>[/<RRTYPE>]')
	parser.add_option('-i', '--rdataip', dest='rdata_ip', type='string',
		help='rdata ip <IPADDRESS|IPRANGE|IPNETWORK>')
	parser.add_option('-s', '--sort', dest='sort', type='string', help='sort key')
	parser.add_option('-R', '--reverse', dest='reverse', action='store_true', default=False,
		help='reverse sort')
	parser.add_option('-j', '--json', dest='json', action='store_true', default=False,
		help='output in JSON format')
	parser.add_option('-l', '--limit', dest='limit', type='int', default=0,
		help='limit number of results')
		
	options, args = parser.parse_args()
	if args:
		parser.print_help()
		sys.exit(1)
	"""	

	cfg = config['pDNS/apikey']
	srv = DEFAULT_DNSDB_SERVER

	client = DnsdbClient(srv, cfg)
	if opt == '-r':
		res_list = client.query_rrset(sub)
	elif opt == '-n':
		res_list = client.query_rdata_name(*sub.split('/'))
	elif opt == '-i':
		res_list = client.query_rdata_ip(sub)
	else:
		parser.print_help()
		sys.exit(1)
	
	fmt_func = lambda x: x

	if len(res_list) > 0:
		if sor == 'y':
			if not sor in res_list[0]:
				sort_keys = res_list[0].keys()
				sort_keys.sort()
				sys.stderr.write('isc_dnsdb_query: invalid sort key "%s". valid sort keys are %s\n' % (sor, ', '.join(sort_keys)))
				sys.exit(1)
			res_list.sort(key=lambda r: r[sor], reverse=options.reverse)

	return res_list