from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('show_recipes', show_recipes, name='show_recipes'),
    path('search/', search, name='search'),
    path('registration/sign_up/', sign_up, name='sign_up'),
    path('user_account', user_account, name='user_account'),
    path('show_recipe/<int:id>', show_recipe, name='show_recipe'),
    path('recipes/page<int:page>', show_user_recipes, name='show_user_recipes'),
    path('create_recipes', views.CreateRecipeView.as_view(), name='create_recipes'),
    path('edit_recipe/<int:id>', views.EditRecipe.as_view(), name="edit_recipe"),
    path('delete_recipe/<int:id>', views.DeleteRecipe.as_view(), name='delete_recipe'),
    path('appetizers', appetizers, name='appetizers'),
    path('desserts', desserts, name='desserts'),
    path('soups', soups, name='soups'),
    path('meat', meat, name='meat'),
    path('vegetarian', vegetarian, name='vegetarian'),
    path('sauces', sauces, name='sauces'),
    path('side_dishes', side_dishes, name='side_dishes'),
]
