from django.conf.urls import url
from MyRecipeApp import views
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.RecipeBook, name='RecipeBook'),
    url(r'^MyRecipeApp/(\d+)/$', views.ViewList, name='viewlist'),
    url(r'^MyRecipeApp/newlist_url$', views.NewList, name='newlist'),
    url(r'^MyRecipeApp/(\d+)/addDish$', views.AddDish, name='addDish'),
    url('admin/', admin.site.urls),
]