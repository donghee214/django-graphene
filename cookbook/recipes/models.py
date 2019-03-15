# cookbook/ingredients/models.py
from django.db import models
from cookbook.ingredients.models import Ingredient


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    instructions = models.TextField()
    ingredients = models.ManyToManyField(
        Ingredient, related_name='recipes')

    def __str__(self):
        res = dict()
        res['title'] = self.title
        res['instructions'] = self.instructions
        res['ingredients'] = self.ingredients
        print(res)
        return self.title
