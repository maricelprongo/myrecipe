from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException



MyRecipe_WAIT = 2

class MyRecipePageTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()


#	def tearDown(self):
#		self.browser.quit()



	def check_for_recipe(self):
		start_time = time.time()
		while True:
			try:
				table = self.browser.find_element_by_id('recipe')
				rows = table.find_elements_by_tag_name('tr')
				return
			except (AssertionError, WebDriverException) as e:
				if time.time() - start_time > MyRecipe_WAIT:
					raise e
					time.sleep(0.5)


	def test_my_recipe_home_page_views(self):
		#self.browser.get('http://localhost:8000/')
		self.browser.get(self.live_server_url)
		#self.assertIn('My Recipe',self.browser.title)
		#recipe_header = self.browser.find_element_by_tag_name('h1').text
		#self.assertIn('-- My Recipe --', recipe_header)

		fName = self.browser.find_element_by_id('fName')
		self.assertEqual(fName.get_attribute('placeholder'),'Please Enter Your Name')
		fName.send_keys('Maricel Prongo')
		time.sleep(1)

		NameofDish = self.browser.find_element_by_id('NameofDish')
		self.assertEqual(NameofDish.get_attribute('placeholder'),'Please Enter Name of Dish')
		NameofDish.send_keys('Chicken Adobo')
		time.sleep(1)


		MainRecipe = self.browser.find_element_by_id('MainRecipe')
		self.assertEqual(MainRecipe.get_attribute('placeholder'),'Please Enter Main Recipe')
		MainRecipe.send_keys('Chicken')
		time.sleep(1)

		Continue = self.browser.find_element_by_id('Continue')
		Continue.click()
		time.sleep(2)

		Ingredients = self.browser.find_element_by_id('Ingredients')
		self.assertEqual(Ingredients.get_attribute('placeholder'),'Ingredients')
		Ingredients.send_keys('1kl Chicken')
		time.sleep(1)

		Procedures = self.browser.find_element_by_id('Procedures')
		self.assertEqual(Procedures.get_attribute('placeholder'),'Procedures')
		Procedures.send_keys('Prito')
		time.sleep(1)

		Create = self.browser.find_element_by_id('Create')
		Create.click()
		time.sleep(2)


	def test_other_dishes(self):
		self.browser.get(self.live_server_url)
		time.sleep(.1)
		fName = self.browser.find_element_by_id('fName')
		self.assertEqual(fName.get_attribute('placeholder'),'Please Enter Your Name')
		fName.send_keys('Leonalyn Maglines')
		time.sleep(1)

		NameofDish = self.browser.find_element_by_id('NameofDish')
		self.assertEqual(NameofDish.get_attribute('placeholder'),'Please Enter Name of Dish')
		NameofDish.send_keys('Bicol Express')
		time.sleep(1)


		MainRecipe = self.browser.find_element_by_id('MainRecipe')
		self.assertEqual(MainRecipe.get_attribute('placeholder'),'Please Enter Main Recipe')
		MainRecipe.send_keys('Pork')
		time.sleep(1)

		Continue = self.browser.find_element_by_id('Continue')
		Continue.click()
		time.sleep(2)

		Ingredients = self.browser.find_element_by_id('Ingredients')
		self.assertEqual(Ingredients.get_attribute('placeholder'),'Ingredients')
		Ingredients.send_keys('1kl Pork')
		time.sleep(1)

		Procedures = self.browser.find_element_by_id('Procedures')
		self.assertEqual(Procedures.get_attribute('placeholder'),'Procedures')
		Procedures.send_keys('Saute garlic and onion')
		time.sleep(1)

		Create = self.browser.find_element_by_id('Create')
		Create.click()
		time.sleep(2)
#		self.wait_for_the_row('1: Chicken Adobo by Maricel Prongo')
#		viewdish_url = self.browser.current_url
#		self.assertRegex(viewdish_url, '/MyRecipeApp/.+')


		self.browser.quit()
		self.browser = webdriver.Firefox()
		#self.browser.get('http://localhost:8000/')
		self.browser.get(self.live_server_url)
#		recipeBody = self.browser.find_element_by_tag_name('body').text
#		self.assertNotIn('Raymond Loon', recipeBody)
		fName = self.browser.find_element_by_id('fName')
		self.assertEqual(fName.get_attribute('placeholder'),'Please Enter Your Name')
		fName.send_keys('Raymond Loon')
		time.sleep(1)

		NameofDish = self.browser.find_element_by_id('NameofDish')
		self.assertEqual(NameofDish.get_attribute('placeholder'),'Please Enter Name of Dish')
		NameofDish.send_keys('Caldereta')
		time.sleep(1)


		MainRecipe = self.browser.find_element_by_id('MainRecipe')
		self.assertEqual(MainRecipe.get_attribute('placeholder'),'Please Enter Main Recipe')
		MainRecipe.send_keys('Pork')
		time.sleep(1)

		Continue = self.browser.find_element_by_id('Continue')
		Continue.click()
		time.sleep(2)

		Ingredients = self.browser.find_element_by_id('Ingredients')
		self.assertEqual(Ingredients.get_attribute('placeholder'),'Ingredients')
		Ingredients.send_keys('1kl Pork')
		time.sleep(1)

		Procedures = self.browser.find_element_by_id('Procedures')
		self.assertEqual(Procedures.get_attribute('placeholder'),'Procedures')
		Procedures.send_keys('Saute garlic and onion')
		time.sleep(1)

		Create = self.browser.find_element_by_id('Create')
		Create.click()
		time.sleep(2)

#		self.wait_for_the_row('1: Bicol Express')
#		NewRecipe_url= self.browser.current_url
#		self.assertRegex(newdish2_url, '/MyRecipeApp/.+')
#		self.assertNotEqual(viewdish_url, NewRecipe_url)
#		recipeBody = self.browser.find_element_by_tag_name('body').text
#		self.assertNotIn('Chicken Adobo', recipeBody)
#		self.assertIn('Bicol Express', recipeBody)







#if __name__=='__main__':
#	unittest.main()

