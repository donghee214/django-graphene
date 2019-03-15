import graphene
from cookbook.recipes.models import Recipe
from cookbook.ingredients.graphqlTypes import IngredientType
from cookbook.recipes.serializers import RecipeSerializer
from graphene_django.rest_framework.mutation import SerializerMutation


class MutateRecipe(SerializerMutation):
    ingredients = graphene.List(IngredientType)

    class Meta:
        serializer_class = RecipeSerializer

    def resolve_ingredients(self, info):
        return self.ingredients.all()


class Mutation(graphene.ObjectType):
    mutate_recipe = MutateRecipe.Field()
