from django.conf.urls import url
from MyRecipeApp import views

urlpatterns = [
    url(r'^$', views.my_recipe, name='my_recipe'),
]
