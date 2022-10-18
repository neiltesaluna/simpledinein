from django.db import models

class Recipe(models.Model):
  title = models.CharField(max_length=150)
  summary = models.TextField(max_length=1000)
  content = models.TextField()

  def __str__(self):
    return self.title