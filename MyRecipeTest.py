from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class MyRecipe(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


	def check_for_the_row(self, row_text):
		table = self.browser.find_element_by_id('DishName')
		rows = table.find_element_by_tag_name('tr')
#		self.assertIn(row_text, [row.text for row in rows])

	def test_type_of_dish_list(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('My Recipe', self.browser.title)
		MyRecipe = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('-- My Recipe --', MyRecipe)

		NameofDish = self.browser.find_element_by_id('NameofDish')
		self.assertEqual(NameofDish.get_attribute('placeholder'), 'Please Enter Name of Dish')
		
		dishName = self.browser.find_element_by_id('NameofDish')
		time.sleep(1)
		dishName.click()
		time.sleep(1)
		dishName.send_keys('Chicken Adobo')
		time.sleep(1)

		authorName = self.browser.find_element_by_id('Name')
		time.sleep(1)
		authorName.click()
		time.sleep(1)
		authorName.send_keys('Maricel Prongo')
		time.sleep(1)




#		Name = self.browser.find_element_by_id('Name')
#		self.assertEqual(Name.get_attribute('placeholder'), 'Please Enter Your Name')
#		Name.send_keys('Maricel Prongo')
#		Name.send_keys(Keys.ENTER)
#		time.sleep(1)

		create = self.browser.find_element_by_id('Create')
		create.click()
		time.sleep(2)
		self.check_for_the_row('1: Chicken Adobo by Maricel Prongo')



		dishName = self.browser.find_element_by_id('NameofDish')
		time.sleep(1)
		dishName.click()
		time.sleep(1)
		dishName.send_keys('Bicol Express')
		time.sleep(1)

		authorName = self.browser.find_element_by_id('Name')
		time.sleep(1)
		authorName.click()
		time.sleep(1)
		authorName.send_keys('Leonalyn Maglines')
		time.sleep(1)


		create = self.browser.find_element_by_id('Create')
		create.click()
		time.sleep(2)
		self.check_for_the_row('1: Chicken Adobo by Maricel Prongo')
		self.check_for_the_row('2: Bicol Express by Leonalyn Maglines')




		table = self.browser.find_element_by_id('DishName')
		rows = table.find_element_by_tag_name('tr')
#		self.assertIn('1: Adobo by Maricel Prongo', [row.text for row in rows])

if __name__=='__main__':
	unittest.main()