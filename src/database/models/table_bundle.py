from sqlalchemy import Table, Column, Float, String, Date, Integer, Boolean

bundle_table = Table(
    "bundle",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("amount_spent", Float, description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0"),
    # TODO: foreign key
    Column("product ",  Field, Product, description="The metadata associated with this Bundle which HumbleBundle calls a Product"),
    Column("gamekey ",  String, description="A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'"),
    Column("uid ",  String, description="A unique identifier for this Bundle used for several purposes in the HumbleBundle API.  Ex: 'X9GHPP9ABKS28'"),
    # TODO: foreign key
    Column("all_coupon_data ",  List, Field(CouponType), description="A list of coupons which came with this bundle."),
    Column("created ",  Date, description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'"),
    # missed_credit= null  # TODO: what is the type of missed_credit ?  What is its purpose?
    # TODO: foreign key
    Column("subproducts ",  List, Field(SubProductType), description="A list of sub-products.  These are like downloadable games, books, etc.")  # TODO: what is a sub product and how does it differ from a product?
    Column("total_choices ", Integer, description="TODO: What does this field do?")  # TODO: properly describe total choices
    # TODO: foreign key
    Column("tpkd_dict ",  Field, TpkdDictType, description="TODO: What a tpkd and what is a tpkd dict?")  # TODO: Properly describe what a TPKD is and what this dict is for
    Column("choices_remaining ",  Integer, description="TODO: What are the 'choices' this refers to?")  # TODO: what are choices?sd
    Column("currency ",  String, description="A string representation of the currency, for example 'USD'")
    Column("is_giftee ",  Boolean, description="Was this product given as a gift to the current user?")
    Column("claimed ",  Boolean, description="Is this bundle claimed already by the current user?")
    Column("total ",  Float, description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0 (TODO: how is this different from amount spent?)")  # TODO: how is total and amount_spent different?
    # TODO: foreign key
    Column("path_ids ",  List, String(description="The path id"), description="The path ids TODO: what are Path IDs?  Are they the ID of this humble bundle for API calls?"))
