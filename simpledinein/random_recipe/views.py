from django.shortcuts import render
from multiprocessing import context
import requests

# Create your views here.
def random(request):
  # setting up drink response from api
  drink_url = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
  drink_response = requests.get(drink_url).json()
  drink_json = drink_response['drinks'][0]
  drink_strIngredient =  [drink_json["strIngredient1"], drink_json["strIngredient2"], drink_json["strIngredient3"], 
                        drink_json["strIngredient4"], drink_json["strIngredient5"], drink_json["strIngredient6"], 
                        drink_json["strIngredient7"], drink_json["strIngredient8"], drink_json["strIngredient9"],
                        drink_json["strIngredient10"], drink_json["strIngredient11"], drink_json["strIngredient12"],
                        drink_json["strIngredient13"], drink_json["strIngredient14"], drink_json["strIngredient15"]]

  drink_strMeasure =  [drink_json["strMeasure1"], drink_json["strMeasure2"], drink_json["strMeasure3"], 
                        drink_json["strMeasure4"], drink_json["strMeasure5"], drink_json["strMeasure6"], 
                        drink_json["strMeasure7"], drink_json["strMeasure8"], drink_json["strMeasure9"],
                        drink_json["strMeasure10"], drink_json["strMeasure11"], drink_json["strMeasure12"],
                        drink_json["strMeasure13"], drink_json["strMeasure14"], drink_json["strMeasure15"]]

  drink_ingredients = {key:value for key,value in zip(drink_strIngredient, drink_strMeasure) if key != None and value != None}


  # setting up meal response from api
  meal_url = "https://www.themealdb.com/api/json/v1/1/random.php"
  meal_response = requests.get(meal_url).json()
  meal_json = meal_response['meals'][0]
  meal_strIngredient =  [meal_json["strIngredient1"], meal_json["strIngredient2"], meal_json["strIngredient3"], 
                        meal_json["strIngredient4"], meal_json["strIngredient5"], meal_json["strIngredient6"], 
                        meal_json["strIngredient7"], meal_json["strIngredient8"], meal_json["strIngredient9"],
                        meal_json["strIngredient10"], meal_json["strIngredient11"], meal_json["strIngredient12"],
                        meal_json["strIngredient13"], meal_json["strIngredient14"], meal_json["strIngredient15"],
                        meal_json["strIngredient16"], meal_json["strIngredient17"], meal_json["strIngredient18"],
                        meal_json["strIngredient19"], meal_json["strIngredient20"]]

  meal_strMeasure =  [meal_json["strMeasure1"], meal_json["strMeasure2"], meal_json["strMeasure3"], 
                        meal_json["strMeasure4"], meal_json["strMeasure5"], meal_json["strMeasure6"], 
                        meal_json["strMeasure7"], meal_json["strMeasure8"], meal_json["strMeasure9"],
                        meal_json["strMeasure10"], meal_json["strMeasure11"], meal_json["strMeasure12"],
                        meal_json["strMeasure13"], meal_json["strMeasure14"], meal_json["strMeasure15"],
                        meal_json["strMeasure16"], meal_json["strMeasure17"], meal_json["strMeasure18"],
                        meal_json["strMeasure19"], meal_json["strMeasure20"]]

  meal_ingredients = {key:value for key,value in zip(meal_strIngredient, meal_strMeasure) if key != "" and value != ""}
    
  context = {
    'drink_json': drink_json,
    'drink_ingredients': drink_ingredients,
    'meal_json': meal_json,
    'meal_ingredients': meal_ingredients,
  }
  return render(request,'random_recipe/random.html', context)