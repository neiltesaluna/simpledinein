from django.urls import path
from . import views

urlpatterns = [
    path('random/', views.random, name='random_recipe')
]