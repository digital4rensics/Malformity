#! /usr/bin/env python

import mechanize
from canari.framework import configure #, superuser
from canari.config import config
from canari.maltego.message import MaltegoException

__author__ = 'Keith Gilbert - @digital4rensics'
__copyright__ = 'Copyright 2013, Malformity Project'
__credits__ = []

__license__ = 'GPL'
__version__ = '0.1'
__maintainer__ = 'Keith Gilbert - @digital4rensics'
__email__ = 'Keith@digital4rensics.com'
__status__ = 'Development'

__all__ = [
    'build',
]

def loginSearch(hash):
	url = 'https://fileadvisor.bit9.com/Services/login.aspx'
	ua = [('User-agent','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)')]

	browse = mechanize.Browser()
	browse.addheaders = ua
	browse.open(url)
	browse.select_form("aspnetForm")
	browse.set_all_readonly(False)
	
	un = config['bit9/username']
	pw = config['bit9/password']
	if un == "<YOUR USERNAME HERE>" or pw == "<YOUR PASSWORD HERE>":
		raise MaltegoException("Please specify Username and Password in config")
	
	browse["__EVENTTARGET"] = ""
	browse["__EVENTARGUMENT"]= ""
	browse["ctl00$ColumnBody$TextBox_UserName"] = un
	browse["ctl00$ColumnBody$TextBox_Password"] = pw
	
	browse.submit(name="ctl00$ColumnBody$Button_Submit")
	
	browse.select_form("aspnetForm")
	browse.set_all_readonly(False)
	
	browse["__EVENTTARGET"] = ""
	browse["__EVENTARGUMENT"]= ""
	browse["ctl00$ColumnBody$RadComboBox1_input"] = hash
	browse["submitbt"] = "Search &raquo;"
	
	results = browse.submit()
	return results.read()