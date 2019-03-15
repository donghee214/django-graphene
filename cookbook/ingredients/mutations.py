import graphene

from cookbook.ingredients.models import Category, Ingredient
from cookbook.ingredients.serializers import IngredientSerializer, CategorySerializer
from cookbook.ingredients.graphqlTypes import CategoryType, IngredientType
from graphene_django.rest_framework.mutation import SerializerMutation


class MutateCategory(SerializerMutation):
    class Meta:
        serializer_class = CategorySerializer


class MutateIngredient(SerializerMutation):
    class Meta:
        serializer_class = IngredientSerializer
    category = graphene.Field(CategoryType)


class Mutation(graphene.ObjectType):
    mutate_ingredient = MutateIngredient.Field()
    mutate_category = MutateCategory.Field()
