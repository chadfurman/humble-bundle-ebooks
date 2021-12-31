from sqlalchemy import Column, Float, String, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from .base import Base
from dto.bundle import Bundle as BundleDTO

BUNDLE_ID_DESCRIPTION = "The unique auto-incrementing ID of this bundle in our local database -- not used by Humble Bundle"
BUNDLE_NAME_DESCRIPTION = "A human-readable name for this bundle"
AMOUNT_DESC_DESCRIPTION = "the amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0"
GAMEKEY_DESCRIPTION = "A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'"
UID_DESCRIPTION = "A unique identifier for this Bundle used for several purposes in the HumbleBundle API.  Ex: 'X9GHPP9ABKS28'"
CREATED_DESCRIPTION = "The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'"
TOTAL_CHOICES_DESCRIPTION = "TODO: What does this field do?"
CHOICES_REMAINING_DESCRIPTION = "TODO: What are the 'choices' this refers to?"
CURRENCY_DESCRIPTION = "A string representation of the currency, for example 'USD'"
IS_GIFTEE_DESCRIPTION = "Was this product given as a gift to the current user?"
CLAIMED_DESCRIPTION = "Is this bundle claimed already by the current user?"
PATH_IDS_DESCRIPTION = "The path ids TODO: what are Path IDs?  Are they the ID of this humble bundle for API calls?"
TOTAL_DESCRIPTION = "The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0 (TODO: how is this different from amount spent?"


class Bundle(Base):
    __tablename__ = "bundles"
    bundle_id = Column(Integer, primary_key=True, comment=BUNDLE_ID_DESCRIPTION, doc=BUNDLE_ID_DESCRIPTION)
    bundle_name = Column(String, comment=BUNDLE_NAME_DESCRIPTION, doc=BUNDLE_NAME_DESCRIPTION)
    amount_spent = Column(Float, doc=AMOUNT_DESC_DESCRIPTION, comment=AMOUNT_DESC_DESCRIPTION)
    gamekey=Column(String, doc=GAMEKEY_DESCRIPTION, comment=GAMEKEY_DESCRIPTION)
    uid=Column(String, doc=UID_DESCRIPTION, comment=UID_DESCRIPTION)
    created=Column(Date, doc=CREATED_DESCRIPTION, comment=CREATED_DESCRIPTION)
    total_choices=Column(Integer, doc=TOTAL_CHOICES_DESCRIPTION, comment=TOTAL_CHOICES_DESCRIPTION)  # TODO: properly describe total choices
    choices_remaining=Column(Integer, doc=CHOICES_REMAINING_DESCRIPTION, comment=CHOICES_REMAINING_DESCRIPTION)  # TODO: what are choices?sd
    currency=Column(String, doc=CURRENCY_DESCRIPTION, comment=CURRENCY_DESCRIPTION)
    is_giftee=Column(Boolean, doc=IS_GIFTEE_DESCRIPTION, comment=IS_GIFTEE_DESCRIPTION)
    claimed=Column(Boolean, doc=CLAIMED_DESCRIPTION, comment=CLAIMED_DESCRIPTION)
    total=Column(Float, doc=TOTAL_DESCRIPTION, comment=TOTAL_DESCRIPTION)  # TODO: how is total and amount_spent different?"
    path_ids=Column(String, doc=PATH_IDS_DESCRIPTION, comment=PATH_IDS_DESCRIPTION)
    # missed_credit= null  # TODO: what is the type of missed_credit ?  What is its purpose?
    # TODO: foreign key, list
    # path_ids = String(description="The path ids TODO: what are Path IDs?  Are they the ID of this humble bundle for API calls?")
    # product = relationship(Product, description="The metadata associated with this Bundle which HumbleBundle calls a Product")
    # all_coupon_data = relationship(CouponType, description="A list of coupons which came with this bundle.")
    # sub_products = relationship(SubProduct, description="A list of sub-products.  These are like downloadable games, books, etc.")  # TODO: what is a sub product and how does it differ from a product?
    # tpkd_dict = relationship(TpkdDict, description="TODO: What a tpkd and what is a tpkd dict?")  # TODO: Properly describe what a TPKD is and what this dict is for
