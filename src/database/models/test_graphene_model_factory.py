import pytest
import sqlalchemy

from .graphene_model_factory import GrapheneModelFactory
from graphene import ObjectType, String, Float, Date, Int, Boolean, ID

class FakeGrapheneType(ObjectType):
    """The GraphQL Bundle type represents a Bundle the authenticated user has in their library"""
    bundle_id = ID(description="A unique identifier for this type in the system")
    amount_spent = Float(
        description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0")
    gamekey = String(
        description="A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'")
    created = Date(
        description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'")
    total_choices = Int(description="TODO: What does this field do?")  # TODO: properly describe total choices
    claimed = Boolean(description="Is this bundle claimed already by the current user?")


def test_graphene_model_factory_makes_model():
    model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
    assert model is not None


def test_graphene_model_factory_inflects_table_name():
    model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
    assert model.__tablename__ == "fake_graphene_types"


def test_graphene_model_factory_converts_scalar_ID():
    model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
    assert model.bundle_id.comparator.primary_key is True, "Bundle ID should be a primary key" # ID(description="A unique identifier for this type in the system")
    assert type(model.bundle_id.comparator.type).__name__ is "Integer", "Bundle ID should be an integer type"
    assert model.bundle_id.comparator.comment is FakeGrapheneType.bundle_id.kwargs['description'], "Bundle ID should have a description that matches the graphene type's description"

def test_graphene_model_factory_converts_scalar_String():
    model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
    typeinfo = model.gamekey.comparator
    assert typeinfo.primary_key is True, "Bundle ID should be a primary key"  # ID(description="A unique identifier for this type in the system")
    assert type(typeinfo.type).__name__ is "String", "Bundle ID should be an integer type"
    assert typeinfo.comment is FakeGrapheneType.gamekey.kwargs['description'], "Bundle ID should have a description that matches the graphene type's description"

def test_graphene_model_factory_converts_scalar_Float():
    model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
    typeinfo = model.amount_spent.comparator
    assert typeinfo.primary_key is True, "Bundle ID should be a primary key"  # ID(description="A unique identifier for this type in the system")
    assert type(typeinfo.type).__name__ is "String", "Bundle ID should be an integer type"
    assert typeinfo.comment is FakeGrapheneType.gamekey.kwargs[
            'description'], "Bundle ID should have a description that matches the graphene type's description"
    # assert model.amount_spent is ... # Float( description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0")
    # assert model.created is ... # Date( description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'")
    # assert model.total_choices is ... # Int(description="TODO: What does this field do?")  # TODO: properly describe total choices
    # assert model.claimed is ... # Boolean(description="Is this bundle claimed already by the current user?")
# #
# #
# # def test_graphene_model_factory_makes_model_with_queryset():
#     # model = GrapheneModelFactory.make_graphene_model(FakeGrapheneType)
#     # assert type(model.objects) == QuerySet
