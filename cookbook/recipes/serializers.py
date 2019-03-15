from rest_framework import serializers
from cookbook.recipes.models import Recipe
from cookbook.ingredients.models import Ingredient
from rest_framework.response import Response
from cookbook.ingredients.serializers import IngredientSerializer


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = serializers.ListField()

    class Meta:
        model = Recipe
        fields = ('id', 'title', 'instructions', 'ingredients')

    def create(self, validated_data):
        recipe_instance = Recipe(
            title=validated_data['title'], instructions=validated_data['instructions'])
        recipe_instance.save()
        query_set = Ingredient.objects.filter(
            pk__in=validated_data['ingredients'])
        recipe_instance.ingredients.set(query_set)
        return recipe_instance

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.email)
        instance.instructions = validated_data.get(
            'instructions', instance.instructions)
        instance.ingredients = validated_data.get(
            'ingredients', instance.ingredients)
        instance.save()
        return instance
