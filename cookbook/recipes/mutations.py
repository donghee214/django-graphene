import graphene
from cookbook.recipes.models import Recipe
from cookbook.recipes.graphqlTypes import RecipeType
from cookbook.ingredients.mutations import IngredientInput
from cookbook.ingredients.models import Ingredient


class RecipeInput(graphene.InputObjectType):
    title = graphene.String()
    instructions = graphene.String()
    ingredients = graphene.List(graphene.ID)


class CreateRecipe(graphene.Mutation):
    class Arguments:
        input = RecipeInput(required=True)
    ok = graphene.Boolean()
    recipe = graphene.Field(RecipeType)

    @staticmethod
    def mutate(self, info, input=None):
        ok = True
        recipe_instance = Recipe(
            title=input.title, instructions=input.instructions)
        recipe_instance.save()
        ingredients = list(Ingredient.objects.filter(pk__in=input.ingredients))
        recipe_instance.ingredients.add(*ingredients)
        return CreateRecipe(ok=ok, recipe=recipe_instance)


class UpdateRecipe(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = RecipeInput()
    ok = graphene.Boolean()
    recipe = graphene.Field(RecipeType)

    @staticmethod
    def mutate(self, info, id, input=None):
        ok = False
        recipe_instance = Recipe.objects.get(pk=id)
        if not recipe_instance:
            return UpdateRecipe(ok=ok, recipe=None)
        ok = True
        if input.title:
            recipe_instance.title = input.title
        if input.instructions:
            recipe_instance.instructions = input.instructions
        if input.ingredients:
            ingredients = list(Ingredient.objects.filter(
                pk__in=input.ingredients))
            recipe_instance.ingredients.set(ingredients)
        recipe_instance.save()
        return UpdateRecipe(ok=ok, recipe=recipe_instance)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()
    update_recipe = UpdateRecipe.Field()
