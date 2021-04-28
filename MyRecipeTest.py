from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class MyRecipe(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

#	def tearDown(self):
#		self.browser.quit()

	def test_this_is_for_the_home_page(self):
		self.browser.get('http://127.0.0.1:8000')
		self.assertIn('My Recipe', self.browser.title)
		MyRecipe = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('My Recipe', MyRecipe)
		
		TypeOfDish = self.browser.find_element_by_id('TypeOfDish')
		self.assertEqual(TypeOfDish.get_attribute('placeholder'), 'Please Enter Type of Dish')
		TypeOfDish.send_keys('Meat')
		TypeOfDish.send_keys(Keys.ENTER)
		time.sleep(1)

		NameOfDish = self.browser.find_element_by_id('NameOfDish')
		self.assertEqual(NameOfDish.get_attribute('placeholder'), 'Please Enter Name of Dish')
		NameOfDish.send_keys('Bicol Express')
		NameOfDish.send_keys(Keys.ENTER)
		time.sleep(1)

		Ingredients = self.browser.find_element_by_id('Ingredients')
		Ingredients.send_keys('Ingredients Dito')
		Ingredients.send_keys(Keys.ENTER)
		time.sleep(1)

		Procedures = self.browser.find_element_by_id('Procedures')
		Procedures.send_keys('Procedures Dito')
		Procedures.send_keys(Keys.ENTER)
		time.sleep(1)

		Name = self.browser.find_element_by_id('Name')
		self.assertEqual(Name.get_attribute('placeholder'), 'Please Enter Your Name')
		Name.send_keys('Maricel Prongo')
		Name.send_keys(Keys.ENTER)
		time.sleep(1)



#		self.fail('Finish the test')

if __name__=='__main__':
	unittest.main()
