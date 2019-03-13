import graphene
from cookbook.recipes.models import Recipe
from cookbook.recipes.graphqlTypes import RecipeType


class Query(object):
    all_recipes = graphene.List(RecipeType)
    recipe = graphene.Field(RecipeType, id=graphene.ID())

    def resolve_all_recipes(self, info, **kwargs):
        return Recipe.objects.all()

    def resolve_recipe(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Recipe.objects.get(pk=id)
