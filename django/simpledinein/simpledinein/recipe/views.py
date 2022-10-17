from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

def home(request):
  return render(request, 'recipe/home.html', context = {'recipes': Recipe.objects.all()})

class RecipeListView(ListView):
  model = Recipe
  template_name = 'recipe/home.html'
  context_object_name = 'recipes'
  ordering = ['title']

class RecipeDetailView(DetailView):
  model = Recipe