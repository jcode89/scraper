import requests
from bs4 import BeautifulSoup

url = "http://www.npr.org/sections/politics/" # use ('div', {'id':'overflow'}) or ('section', {'id':'archive-core'})
#url = 'https://www.youtube.com/' # use ('div',{'id':'page'})
tag = 'section'	
filename = 'npr_test.txt'
file = 'npr_links.txt'
# Opens and obtains the information from the site.
# Reads through and obtains the information in the overflow id.
# Loops through the information writing it to a file after turning it to a string and splitting it.	
def scrape(url, tag):
	site = requests.get(url)
	words = site.text
	soup = BeautifulSoup(words)
	with open(filename, 'wb') as f:
		for item in soup.find(tag, {'id':'archive-core'}):
			new_item = (str(item))
			print new_item
			for text in new_item:
				f.write(text)

# Creates an empty dictionary				
fin = {}
# Rewrites the data from the file created by scrape and adds the data to the dictionary.
def rewrite(filename):
	with open(filename, 'r') as n:
		key = ''
		for lines in n:
			if 'href' in lines:
				key = lines[lines.find('href'):]
				value = lines[:lines.find('href')]
				print (key, value)
				fin[key] = [value]

# Creates a new file and saves the keys from the dictionary fin to it.				
def new_file(file):
	with open(file, 'w') as m:
		for piece in fin:
			m.write(('#[{}]\n').format(piece))

# This piece of code works when run, but manually entering into the code is easier since it is in alpha.			
#url = raw_input('Enter the URL: ')			
scrape(url, tag)
rewrite(filename)
new_file(file)
print fin
	
	
# Similar to the code above, however, urllib2 is used instead of requests.
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
link = urlopen('http://kjaymiller.com/')
soup = BeautifulSoup(link.read())
#print soup
lister = {}
for stuff in soup.find('section',{'class':'post-excerpt'}):
	print stuff
	
	#lister.update({stuff:'none'})
#new_lister = ''
#for item in lister:
		#new_lister = new_lister + '{}\n'.format(item)
	
#print new_lister