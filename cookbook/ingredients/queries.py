# cookbook/ingredients/schema.py
import graphene
from cookbook.ingredients.models import Category, Ingredient
from cookbook.ingredients.graphqlTypes import CategoryType, IngredientType


class Query(object):
    all_categories = graphene.List(CategoryType)
    all_ingredients = graphene.List(IngredientType)
    category = graphene.Field(
        CategoryType, id=graphene.ID())
    ingredient = graphene.Field(
        IngredientType, id=graphene.ID())

    def resolve_all_categories(self, info, **kwargs):
        return Category.objects.all()

    def resolve_all_ingredients(self, info, **kwargs):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related('category').all()

    def resolve_category(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Category.objects.get(pk=id)

    def resolve_ingredient(self, into, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return Ingredient.objects.get(pk=id)
