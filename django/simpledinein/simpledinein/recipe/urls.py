from django.urls import path
from . import views

urlpatterns = [
    path('recipe/', views.recipe, name='recipe_view'),
]