from django.shortcuts import render
from multiprocessing import context
import requests

# Create your views here.
def random(request):
  # setting up drink response from api
  drink_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
  drink_response = requests.get(drink_url).json()
  drink_json = drink_response['drinks'][0]
  
  drink_strIngredient = [drink_json["strIngredient" + str(i)] for i in range(1,16)]
  drink_strMeasure = [drink_json["strMeasure" + str(i)] for i in range(1,16)]
  
  drink_ingredients = {key:value for key,value in zip(drink_strIngredient, drink_strMeasure) if key != None and value != None}

  # setting up meal response from api
  meal_url = "https://www.themealdb.com/api/json/v1/1/random.php"
  meal_response = requests.get(meal_url).json()
  meal_json = meal_response['meals'][0]
  
  meal_strIngredient = [meal_json["strIngredient" + str(i)] for i in range(1,21)]
  meal_strMeasure = [meal_json["strMeasure" + str(i)] for i in range(1,21)]
  
  meal_ingredients = {key:value for key,value in zip(meal_strIngredient, meal_strMeasure) if key != "" and value != ""}
    
  context = {
    'drink_json': drink_json,
    'drink_ingredients': drink_ingredients,
    'meal_json': meal_json,
    'meal_ingredients': meal_ingredients,
  }
  return render(request,'random_recipe/random.html', context)
