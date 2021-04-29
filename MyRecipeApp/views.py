from django.shortcuts import render, redirect
#from django.http import HttpResponse
from MyRecipeApp.models import Dish

def my_recipe(request):
	if request.method == 'POST':
#		newDish = request.POST['NameofDish']
		Dish.objects.create(text=request.POST['NameofDish'])
		return redirect('/')
	dishes = Dish.objects.all()
#	else:
#		newDish=""
	return render(request, 'homepage.html', {'newDishName': dishes,})



#	dish1 = Dish()
#	dish1.text=request.POST.get('NameofDish', '')
#	dish1.save()
#	dish2 = Dish()
#	dish2.text=request.POST.get('Name', '')
#	dish2.save()
#	return render(request, 'homepage.html', {'newDishName': dish1.text, 'newName': dish2.text,})


#	return render(request, 'homepage.html', {'newDishName':request.POST.get('NameofDish'),})# 'newName':request.POST.get('Name'),})


#	if request.method == 'POST':
#		return HttpResponse(request.POST['NameofDish'])
#	return render(request, 'homepage.html')