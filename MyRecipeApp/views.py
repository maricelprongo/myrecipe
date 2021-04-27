from django.shortcuts import render
#from django.http import HttpResponse


def my_recipe(request):
	return render(request, "homepage.html")