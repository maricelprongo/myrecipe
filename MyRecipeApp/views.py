from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyRecipeApp.models import Dish, MRecipe




def my_recipe(request):
	dishes = Dish.objects.all()
	return render(request, 'homepage.html',{'dishes' : dishes})




def ViewRecipe(request, recipe_id):
	recipe = MRecipe.objects.get(id=recipe_id)
	return render(request, 'next.html', {'recipe': recipe})


def NewRecipe(request):
    recipe = MRecipe.objects.create()
    Dish.objects.create(rName=request.POST['fName'],rNameofDish =request.POST['NameofDish'],rMainRecipe=request.POST['MainRecipe'], recipe=recipe)
    return redirect(f'/MyRecipeApp/{recipe.id}/')

def AddRecipe(request, recipe_id):
    recipe = MRecipe.objects.get(id=recipe_id)
    Dish.objects.create(rIngredients=request.POST['Ingredients'],rProcedures =request.POST['Procedures'], recipe=recipe)
    return redirect(f'/MyRecipeApp/{recipe.id}/')



