from bs4 import BeautifulSoup
import requests
import re

class Scrape():
    def __init__(self, site_name=input, rspns=input, display=print):
        self.site_name = site_name
        self.rspns = rspns
        self.display = display
        self.birth_date = []
    def grab_birth_year(self):
        self.name = self.site_name("Please enter name like this: First_Last:\n")
        self.url = requests.get('https://en.wikipedia.org/wiki/'+ self.name)
        self.soup = BeautifulSoup(self.url.text)
        stuff = self.soup.find_all("span", class_="bday")
        num = re.compile('[0-9]{4}')
        try:
            for item in stuff:
                birth = item.get_text()
                
                for date in birth:
                   self.birth_date.append(date)
            self.date_of_birth = len("".join(self.birth_date)) # length of list should be 10
            birth = num.match(birth)
            birth_prime = birth.group()
            return self.display("Born: %s" % birth_prime), self.date_of_birth # prints out the year
        except UnboundLocalError:       
            try:
                new_stuff = self.soup.find("tr")
                n_birth = new_stuff.next_sibling.next_sibling.next_sibling.next_sibling
                self.display(n_birth.next_element.next_element.next_element.next_element.next_element.next_element)
                resp = self.rspns("Did it work?\n").lower()
                
                if resp == "yes":
                    exit(0)
                elif resp == "no":
                    self.display("Here we are: %s" % n_birth.next_element.next_element.next_element.next_element.next_element.next_element.next_element.next_element)				
                    resp = self.rspns("How about that?\n").lower()
                    				
                    if resp == "no":
                        n_birth = new_stuff.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
                        return self.display("Okay here it is: %s" % n_birth.next_element.next_element.next_element.next_element.next_element.next_element)
                    else:
                        exit(0)
            except AttributeError:
                return self.display("Woops! Date unfetchable!")
			
    
#prjct = Scrape()
#prjct.grab_birth_year()