from rest_framework import serializers
from cookbook.ingredients.models import Ingredient, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class IngredientSerializer(serializers.ModelSerializer):
    category = serializers.CharField(max_length=100)

    class Meta:
        model = Ingredient
        fields = ('id', 'name', 'notes', 'category')

    def create(self, validated_data):
        return Ingredient.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.notes = validated_data.get('notes', instance.notes)
        instance.category = Category.objects.get(
            pk=validated_data.get('category', instance.category))
        instance.save()
        return instance
