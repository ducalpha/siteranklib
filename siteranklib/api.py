# -*- coding: UTF-8 -*-

import requests
from lxml import etree

from siteranklib.helpers import get_elements

def get_alexa(url):
	rank = None
	request_url = 'http://xml.alexa.com/data?cli=10&dat=nsa&ver=quirk-searchstatus&url=%s' % url
	popularity = get_elements(request_url, '//POPULARITY', parser=etree.XMLParser(encoding='utf-8'))
	if len(popularity):
		rank = int(popularity[0].get('TEXT'))
	return rank

def get_alexa_us(url):
	rank = None
	request_url = 'http://xml.alexa.com/data?cli=10&dat=nsa&ver=quirk-searchstatus&url=%s' % url
	popularity = get_elements(request_url, '//COUNTRY', parser=etree.XMLParser(encoding='utf-8'))
	if len(popularity):
		rank = int(popularity[0].get('RANK'))
	return rank
