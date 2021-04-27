from selenium import webdriver
import unittest

class MyRecipe(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

#	def tearDown(self):
#		self.browser.quit()

	def test_title_of_the_page(self):
		self.browser.get('http://127.0.0.1:8000')
		self.assertIn('My Recipe', self.browser.title)
		MyRecipe = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('My Recipe', MyRecipe)
#		self.fail('Finish the test')

if __name__=='__main__':
	unittest.main()
