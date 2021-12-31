from graphene import ObjectType, String, Field, Boolean
from schema.types.empty_tpkds import EmptyTpkds


class Product(ObjectType):
    """A product that has been purchased on the Humble Bundle website.  Could be a Bundle, could be something else."""
    category=String(name="category", description="The category of product, for example 'bundle'.  TODO: Make this an enum with known categories")
    machine_name= String(name="machine_name", description="The name that the Humble Bundle system calls this product, for exampel '2danimation_softwarebundle'")
    empty_tpkds= Field(EmptyTpkds,name="empty_tpkds",  description="TODO: What is this field?")
    post_purchase_text= String(name="post_purchase_text", description="TODO: What is this?  I assume it's text that displays on the screen after a bundle is purchased and likely is not important for our purposes?")
    human_name= String(name="human_name", description="The human-readable name of this bundle.  For example: 'Humble Software Bundle: 2D Animation'")
    partial_gift_enabled= Boolean(name="partial_gift_enabled", description="TODO: What's the purpose of this field?")