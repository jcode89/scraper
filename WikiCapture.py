# -*- coding: utf-8 -*-
# ISO-8859-1
from bs4 import BeautifulSoup
import requests
import re

class Scrape():
    def __init__(self, site_name=input):
        self.site_name = site_name
        self.birth_date = []
    def grab_birth_year(self):
        name = self.site_name("Please enter name like this: First_Last:\n")
        self.url = requests.get('https://en.wikipedia.org/wiki/'+ name)
        self.soup = BeautifulSoup(self.url.text)#.decode("utf-8", "ignore")
        stuff = self.soup.find_all("span", class_="bday")
        num = re.compile('[0-9]{4}')
        try:
            for item in stuff:
                birth = item.get_text()
                
                for date in birth:
                   self.birth_date.append(date)#.partition('-')
            birth = num.match(birth)
            print (birth.group())
        except UnboundLocalError:       
            self.grab_birth_year_2()        		
      
        #new_stuff = self.soup.find("tr")
        #n_birth = new_stuff.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
        #print (n_birth)
        #for sibling in self.soup.find("tr").next_siblings:
        #    print (repr(sibling))		
    def grab_birth_year_2(self):
        
        for sibling in self.soup.find("tr").next_siblings:
            print (repr(sibling))
prjct = Scrape()
prjct.grab_birth_year()