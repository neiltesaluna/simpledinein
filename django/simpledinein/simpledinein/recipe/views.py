from django.shortcuts import render
from .models import Recipe

def home(request):
  return render(request, 'recipe/home.html', context = {'recipes': Recipe.objects.all()})
