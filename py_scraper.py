import requests
from bs4 import BeautifulSoup

#url = "http://www.npr.org/sections/politics/" # use ('div', {'id':'overflow'}) or ('section', {'id':'archive-core'})
#url = 'https://www.youtube.com/' # use ('div',{'id':'page'})

# Opens and obtains the information from the site.
# Reads through and obtains the information in the overflow id.
# Loops through the information writing it to a file after turning it to a string and splitting it.	
def get_site(url):
	site = requests.get(url)
	soup = BeautifulSoup(site.content)
	return soup
def scrape_links(soup, tag):
	
	with open(source, 'w') as f:
		for item in soup.find_all(tag, id="archive-core"):
			new_item = (str(item.find_all({'a':'href'})))
			print new_item
			for text in new_item:
				f.write(text)
				
def scrape_text():
	pass
# Creates an empty dictionary				
fin = {}
# Rewrites the data from the file created by scrape and adds the data to the dictionary.
def rewrite(source):
	with open(source, 'r') as n:
		key = ''
		for lines in n:
			if 'href' in lines:
				key = lines[lines.find('http'):]
				value = lines[:lines.find('http')]
				print (key, value)
				fin[key] = [value]

# Creates a new file and saves the keys from the dictionary fin to it.				
def new_file(s_data):
	with open(s_data, 'w') as m:
		for piece in fin:
			m.write(('#[{}]\n').format(piece))

			
url = raw_input('Enter the URL: ')			
tag = 'section'	
source = 'source.txt'
s_data = 'links.txt'
soup = get_site(url)
scrape_links(soup, tag)
rewrite(source)
new_file(s_data)

	
	
