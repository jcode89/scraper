import unittest
from WikiCapture import Scrape

class ScrapeTest(unittest.TestCase):
    def setUp(self):
        self.scrape = Scrape().grab_birth_year()
		
    def tearDown(self):		
        self.scrape = None
		
    def test_grab_birth_year(self):
        
        self.scrape
        
        self.assertEqual(self.scrape, (None, 10))
   
if __name__ == '__main__':
    unittest.main()