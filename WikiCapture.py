from bs4 import BeautifulSoup
import requests
import re

class Scrape():
    def __init__(self, site_name=input, rspns=input):
        self.site_name = site_name
        self.rspns = rspns
        self.birth_date = []
    def grab_birth_year(self):
        name = self.site_name("Please enter name like this: First_Last:\n")
        self.url = requests.get('https://en.wikipedia.org/wiki/'+ name)
        self.soup = BeautifulSoup(self.url.text)
        stuff = self.soup.find_all("span", class_="bday")
        num = re.compile('[0-9]{4}')
        try:
            for item in stuff:
                birth = item.get_text()
                
                for date in birth:
                   self.birth_date.append(date)
            birth = num.match(birth)
            birth_prime = birth.group()
            print ("Born: %s" % birth_prime)
        except UnboundLocalError:       
            try:
                new_stuff = self.soup.find("tr")
                n_birth = new_stuff.next_sibling.next_sibling.next_sibling.next_sibling#.next_sibling.next_sibling
                print (n_birth.next_element.next_element.next_element.next_element.next_element.next_element)
                resp = self.rspns("Did it work?\n").lower()
                if resp == "yes":
                    exit(0)
                elif resp == "no":
                    n_birth = new_stuff.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                    print ("Okay here it is: %s" % n_birth.next_element.next_element.next_element.next_element.next_element.next_element)
            except AttributeError:
                print ("Woops! Date unfetchable!")
			
    
prjct = Scrape()
prjct.grab_birth_year()