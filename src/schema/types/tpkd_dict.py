from graphene import ObjectType, List, Field
from .tpkd import Tpkd

class TpkdDict(ObjectType):
    """Dictionary containing TPKs TODO: What's a TPK?"""
    all_tpks=List(Field(Tpkd), description="All TPKs (TODO: what is this field?")