from django.urls import resolve
from django.test import TestCase
from MyRecipeApp.views import my_recipe
from MyRecipeApp.models import Dish, MRecipe
#from django.http import HttpRequest
#from django.template.loader import render_to_string



class MyRecipeTest(TestCase):


	def test_root_url_resolves_to_my_recipeviews(self):
		found = resolve('/')
		self.assertEqual(found.func, my_recipe)

	def test_only_saves_my_recipewhen_necessary(self):
		self.client.get('/')
		self.assertEqual(Dish.objects.count(), 0)



class MRecipeViewTest(TestCase):


	def test_uses_recipetemplate(self):
		recipe = MRecipe.objects.create()
		response = self.client.get(f'/MyRecipeApp/{recipe.id}/')
		self.assertTemplateUsed(response, 'next.html')

#	def test_displays_all_recipedishes(self):
#		recipe = MRecipe.objects.create()
#		Dish.objects.create(rName='Maricel Prongo',recipe=recipe)



	def test_passes_correct_recipeto_template(self):
		other_recipe = MRecipe.objects.create()
		correct_recipe = MRecipe.objects.create()
		response = self.client.get(f'/MyRecipeApp/{correct_recipe.id}/')
		self.assertEqual(response.context['recipe'], correct_recipe)



class NewMRecipeTest(TestCase):



	def test_redirects_after_POST(self):
		response = self.client.post('/MyRecipeApp/new', data={'fName': 'New Name','NameofDish': 'New Dish','MainRecipe':'New main recipe','Ingredients': 'New Ingredients','Procedures': 'New Procedures'})
		new_recipe = MRecipe.objects.first()
		self.assertRedirects(response, f'/MyRecipeApp/{new_recipe.id}/')


class NewDishTest(TestCase):


	def test_can_save_a_POST_request_to_an_existing_recipe(self):
		other_recipe = MRecipe.objects.create()
		correct_recipe = MRecipe.objects.create()
		self.client.post(f'/MyRecipeApp/{correct_recipe.id}/AddRecipe', data={'fName': 'New Name','NameofDish': 'New Dish','MainRecipe':'New main recipe','Ingredients': 'New Ingredients','Procedures': 'New Procedures'})
		self.assertEqual(Dish.objects.count(), 1)
		new_dish = Dish.objects.first()
		self.assertEqual(new_dish.rName, '')
		self.assertEqual(new_dish.recipe, correct_recipe)

	def test_redirects_to_recipeview(self):        
		other_recipe = MRecipe.objects.create()        
		correct_recipe = MRecipe.objects.create()        
		response = self.client.post(f'/MyRecipeApp/{correct_recipe.id}/AddRecipe', data={'fName': 'New Name','NameofDish': 'New Dish','MainRecipe':'New main recipe','Ingredients': 'New Ingredients','Procedures': 'New Procedures'})
		self.assertRedirects(response, f'/MyRecipeApp/{correct_recipe.id}/')

class Recipe_ORM(TestCase):

	def test_saving_and_retrieving_dishes(self):
		recipe = MRecipe()        
		recipe.save()
		first_dish = Dish()
		first_dish.rName = 'The first recipe owner'
		first_dish.recipe = recipe
		first_dish.save()
		second_dish = Dish()
		second_dish.rName = 'The second recipe owner'
		second_dish.recipe = recipe
		second_dish.save()
		saved_recipe = MRecipe.objects.first()
		self.assertEqual(saved_recipe, recipe)
		saved_dishes = Dish.objects.all()
		self.assertEqual(saved_dishes.count(), 2)
		first_saved_dish = saved_dishes[0]
		second_saved_dish = saved_dishes[1]
		self.assertEqual(first_saved_dish.rName, 'The first recipe owner')
		self.assertEqual(second_saved_dish.rName, 'The second recipe owner')
		self.assertEqual(second_saved_dish.recipe, recipe)






