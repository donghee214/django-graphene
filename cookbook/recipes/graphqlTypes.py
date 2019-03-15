import graphene
from graphene_django.types import DjangoObjectType
from cookbook.recipes.models import Recipe
from cookbook.ingredients.models import Ingredient


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
