from django.db import models

class Recipe(models.Model):
  title = models.CharField(max_length=1000)
  content = models.TextField()