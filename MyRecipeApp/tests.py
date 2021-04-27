from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from MyRecipeApp.views import my_recipe
#from django.core.urlresolvers import resolve


class MyRecipeTest(TestCase):

	def test_url_to_my_home_page(self):
		found = resolve('/')
		self.assertEqual(found.func, my_recipe)

	def test_my_recipe_home_page_view(self):
		request = HttpRequest()
		response = my_recipe(request)
		self.assertTrue(response.content.startswith(b'<html>'))
		self.assertIn(b'<title>My Recipe</title>', response.content)
		self.assertTrue(response.content.endswith(b'</html>'))

	def test_my_recipe_home_page_root(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'homepage.html')
