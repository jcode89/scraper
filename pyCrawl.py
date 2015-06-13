# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq


links = {}
def crawl(url):
	"""Grabs the http links from the site and saves them in a dictionary."""
	site = pq(url)
	value =""
	for link in site('a').items():
		n_link = (str(link.attr['href']))
		print n_link
		if n_link.startswith('http'):
			key = n_link
			links[key] = value
					
def writeTo(filename1):
	"""Saves the key in the dictionary to a file."""
	with open(filename1, 'w') as f:
		for k, v in links.iteritems():
			f.write(('-----[{}]({})\n').format(k, v))

#url = "http://www.datasciencecentral.com/profiles/blogs/50-blogs-worth-reading"
url = raw_input("Enter the URL: ")
#filename1 = 'DataBlogs.txt'
filename1 = 'siteLinks.txt'
crawl(url)
writeTo(filename1)
print links



