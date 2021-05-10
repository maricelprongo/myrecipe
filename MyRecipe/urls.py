from django.conf.urls import url
from MyRecipeApp import views 

urlpatterns = [
	url(r'^$', views.my_recipe, name='my_recipe'),
    url(r'^MyRecipeApp/(\d+)/$', views.ViewRecipe, name='ViewRecipe'),
    url(r'^MyRecipeApp/new$', views.NewRecipe, name='NewRecipe'),
    url(r'^MyRecipeApp/(\d+)/AddRecipe$', views.AddRecipe, name='AddRecipe'),

 ]
    


