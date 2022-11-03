from django.urls import path
from . import views

urlpatterns = [
  path('', views.getData, name='api_link'),
  path('<int:pk>', views.recipeDetail),
]