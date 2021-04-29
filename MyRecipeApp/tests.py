from django.test import TestCase
#from django.urls import resolve
#from MyRecipeApp.views import my_recipe
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from MyRecipeApp.models import Dish

class MyRecipeTest(TestCase):

#	def test_resolver_of_my_recipe_homepage(self):
#		found = resolve ('/')
#		self.assertEqual(found.func, my_recipe)

	def test_my_recipe_home_page_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')

	def test_for_saving_the_POST_request(self):
		response = self.client.post('/', data = {'NameofDish': 'New name of Dish'})
		self.assertEqual(Dish.objects.count(), 1)
		newDish = Dish.objects.first()
		self.assertEqual(newDish.text, 'New name of Dish')

	def test_redirect_POST_req(self):
		response =self.client.post('/', data = {'NameofDish': 'New name of Dish'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


	def test_saves_dishes(self):
		self.client.get('/')
		self.assertEqual(Dish.objects.count(), 0)

	def test_template_display_list(self):
		Dish.objects.create(text='Dish 1')
		Dish.objects.create(text='Dish 2')
		response = self.client.get('/')
		self.assertIn('Dish 1', response.content.decode())
#		self.assertIn('Dish 2', response.content,decode())




class ORMTest(TestCase):

	def test_for_saving_the_list(self):
		inputDish1 = Dish()
		inputDish1.text = 'First Dish'
		inputDish1.save()
		inputDish2 = Dish()
		inputDish2.text = 'Second Dish'
		inputDish2.save()
		savedDishes = Dish.objects.all()
		self.assertEqual(savedDishes.count(),2)
		savedDish1 = savedDishes[0]
		savedDish2 = savedDishes[1]
		self.assertEqual(savedDish1.text, 'First Dish')
		self.assertEqual(savedDish2.text, 'Second Dish')