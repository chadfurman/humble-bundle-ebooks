from schema.types.bundle import Bundle
import graphene.types.scalars as GrapheneScalars
import sqlalchemy
from database.models.base import Base as BaseSqlalchemyModel
import inflect

from utils import to_snake_case

inflector = inflect.engine()


class GrapheneModelFactory():
    @classmethod
    def make_graphene_model(cls, graphene_type):
        graphene_attrs = dir(graphene_type)
        sql_attrs = {}
        for attribute_name in graphene_attrs:
            attribute_value = getattr(graphene_type, attribute_name)
            if GrapheneParser.is_scalar(attribute_value):
                converter = GrapheneParser.get_converter(attribute_value)
                column_definition = converter.convert(attribute_value=attribute_value, attribute_name=attribute_name)
                sql_attrs[attribute_name] = column_definition
        name = graphene_type.__name__
        snake_case_name = to_snake_case(name)

        sql_attrs['__tablename__'] =  inflector.plural(snake_case_name, 2)
        sql_attrs['__repr__'] = lambda self: f"{name}(attrs={sql_attrs.keys()})"
        return type(f"{name}", (BaseSqlalchemyModel,), sql_attrs)


class SQLAlchemyConverter():
    @classmethod
    def _convert(cls, type, attribute_name, attribute_value, **kwargs):
        name=attribute_name
        description = attribute_value.kwargs['description']
        my_kwargs = {
            'name': name,
            'doc': description,
            'comment': description,
        }
        my_kwargs.update(**kwargs)
        return sqlalchemy.Column(type, **my_kwargs)


class StringConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.String):
        return SQLAlchemyConverter._convert(sqlalchemy.String, attribute_value=attribute_value, attribute_name=attribute_name)


class IntConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.Int):
        return SQLAlchemyConverter._convert(sqlalchemy.Integer, attribute_value=attribute_value, attribute_name=attribute_name)


class BigIntConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.BigInt):
        return SQLAlchemyConverter._convert(sqlalchemy.BigInteger, attribute_value=attribute_value, attribute_name=attribute_name)


class FloatConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.Float):
        return SQLAlchemyConverter._convert(sqlalchemy.Float, attribute_value=attribute_value, attribute_name=attribute_name)


class BooleanConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.Boolean):
        return SQLAlchemyConverter._convert(sqlalchemy.Boolean, attribute_value=attribute_value, attribute_name=attribute_name)


class IDConverter():
    @classmethod
    def convert(cls, attribute_name: str, attribute_value: GrapheneScalars.ID):
        return SQLAlchemyConverter._convert(sqlalchemy.Integer, attribute_value=attribute_value, attribute_name=attribute_name, primary_key=True)


class GrapheneParser():
    scalar_types = {GrapheneScalars.String: StringConverter, GrapheneScalars.Int: IntConverter, GrapheneScalars.BigInt: BigIntConverter, GrapheneScalars.Float:FloatConverter, GrapheneScalars.ID:IDConverter}

    @classmethod
    def is_scalar(cls, attr):
        attr_type = type(attr)
        for scaler_type in cls.scalar_types.keys():
            if issubclass(attr_type, scaler_type) or isinstance(attr_type, scaler_type):
                return True
        return False

    @classmethod
    def get_converter(cls, attr):
        attr_type = type(attr)
        for scaler_type in cls.scalar_types.keys():
            if issubclass(attr_type, scaler_type) or isinstance(attr_type, scaler_type):
                return cls.scalar_types[attr_type]