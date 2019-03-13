import graphene

from cookbook.ingredients.models import Category, Ingredient

from cookbook.ingredients.graphqlTypes import CategoryType, IngredientType


class CategoryInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()


class IngredientInput(graphene.InputObjectType):
    id = graphene.ID()
    name = graphene.String()
    notes = graphene.String()
    category = graphene.Field(CategoryInput)


class CreateIngredient(graphene.Mutation):
    class Arguments:
        input = IngredientInput(required=True)

    ok = graphene.Boolean()
    ingredient = graphene.Field(IngredientType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        ingredient_instance = Ingredient(
            name=input.name, notes=input.notes, category=input.category)
        ingredient_instance.save()
        return CreateIngredient(ok=ok, ingredient=ingredient_instance)


class UpdateIngredient(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        input = IngredientInput()

    ok = graphene.Boolean()
    ingredient = graphene.Field(IngredientType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        ingredient_instance = Ingredient.objects.get(pk=id)
        if ingredient_instance:
            ok = True
            if input.name:
                ingredient_instance.name = input.name
            if input.notes:
                ingredient_instance.notes = input.notes
            if input.category:
                ingredient_instance.category = input.category
            ingredient_instance.save()
            return UpdateIngredient(ok=ok, ingredient=ingredient_instance)
        return UpdateIngredient(ok=ok, ingredient=None)


class Mutation(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
