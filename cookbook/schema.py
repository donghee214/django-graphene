import graphene
import cookbook.ingredients.queries
import cookbook.ingredients.mutations
import cookbook.recipes.queries
import cookbook.recipes.mutations


class Queries(cookbook.ingredients.queries.Query,
              cookbook.recipes.queries.Query, graphene.ObjectType):
    pass


class Mutations(cookbook.ingredients.mutations.Mutation,
                cookbook.recipes.mutations.Mutation, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Queries, mutation=Mutations)
