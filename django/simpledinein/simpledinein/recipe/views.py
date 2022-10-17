from django.shortcuts import render
from .models import Recipe

def recipe(request):
  return render(request, 'recipe/recipe.html', context = {'recipes': Recipe.objects.all()})
