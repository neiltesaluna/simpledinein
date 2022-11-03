from rest_framework.response import Response
from rest_framework.decorators import api_view
from recipe.models import Recipe
from .serializers import RecipeSerializers

@api_view(['GET'])
def getData(request):
  items = Recipe.objects.all()
  serializer = RecipeSerializers(items, many=True) # Serializing multiple items 'many=True'
  return Response(serializer.data)

@api_view(['GET'])
def recipeDetail(request, pk): #this pk would be sent from .urls when requested
  item = Recipe.objects.get(pk=pk)
  serializer = RecipeSerializers(item)
  return Response(serializer.data)
