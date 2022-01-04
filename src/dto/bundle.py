from attr import define, field

@define
class Bundle:
    # TODO: foreign key, list
    # product = relationship(Product, description="The metadata associated with this Bundle which HumbleBundle calls a Product")
    # all_coupon_data = relationship(CouponType, description="A list of coupons which came with this bundle.")
    # sub_products = relationship(SubProduct, description="A list of sub-products.  These are like downloadable games, books, etc.")  # TODO: what is a sub product and how does it differ from a product?
    # tpkd_dict = relationship(TpkdDict, description="TODO: What a tpkd and what is a tpkd dict?")  # TODO: Properly describe what a TPKD is and what this dict is for

    bundle_id = field()  # Integer, primary_key=True, description="The unique auto-incrementing ID of this bundle in our local database -- not used by Humble Bundle")
    bundle_name = field()  # String, description="A human-readable name for this bundle")
    amount_spent = field(default=None)  # Float, description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0")
    gamekey = field(default=None)  # String, description="A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'")
    uid = field(default=None)  # String, description="A unique identifier for this Bundle used for several purposes in the HumbleBundle API.  Ex: 'X9GHPP9ABKS28'")
    created = field(default=None)  # Date, description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'")
    #  # missed_credit= null  # TODO: what is the type of missed_credit ?  What is its purpose?
    total_choices = field(default=None)  # Integer, description="TODO: What does this field do?")  # TODO: properly describe total choices
    choices_remaining = field(default=None)  # Integer, description="TODO: What are the 'choices' this refers to?")  # TODO: what are choices?sd
    currency = field(default="")  # String, description="A string representation of the currency, for example 'USD'")
    is_giftee = field(default=False)  # Boolean, description="Was this product given as a gift to the current user?")
    claimed = field(default=None)  # Boolean, description="Is this bundle claimed already by the current user?")
    total = field(default=None)  # Float, description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0 (TODO: how is this different from amount spent?)")  # TODO: how is total and amount_spent different?
    #  # TODO: foreign key, list
    path_ids = field(default=None)  # String, description="The path ids TODO: what are Path IDs?  Are they the ID of this humble bundle for API calls?")

    # def __repr__(self):
    #     return f"Bundle(name={self.bundle_name}, claimed={self.claimed})"

