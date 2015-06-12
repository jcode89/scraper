# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq
links = {}

# There are some extra pieces of code because it is a work in progress.
def crawl(url):
	"""Grabs the http links from the site and saves them in a dictionary."""
	site = requests.get(url)
	items = pq(site.content)
	#print items('a') 
	[a.text for a in items('a')]
	#cup = str(juice)
	#web = pq(url, {'a' : 'href'}, verify = True)
	#print web
	st = pq(url)
	#strts = re.match(r'^http.*\m')
	value =""
	for link in st('a').items():
		n_link = (str(link.attr['href']))
		print n_link
		if n_link.startswith('http'):
			key = n_link
			links[key] = value
			#links.update({key:value})
			
		
def writeTo(filename1):
	"""Saves the key in the dictionary to a file."""
	with open(filename1, 'w') as f:
		for k, v in links.iteritems():
			f.write(('-----[{}]({})\n').format(k, v))

url = "http://www.datasciencecentral.com/profiles/blogs/50-blogs-worth-reading"
#url = raw_input("Enter the URL: ")
filename1 = 'DataBlogs.txt'
crawl(url)
writeTo(filename1)
print links



