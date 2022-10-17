from django.urls import path
from .views import RecipeListView, RecipeDetailView
from . import views

urlpatterns = [
    path('', RecipeListView.as_view(), name='all_recipes'),
    path('<int:pk>', RecipeDetailView.as_view(), name='recipe_detail')
]