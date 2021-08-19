from graphene import ObjectType, List, Field, String, Float, Date, Int, Boolean

class Bundle(ObjectType):
    """The GraphQL Bundle type represents a Bundle the authenticated user has in their library"""
    amount_spent= Float(description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0")
    product=Field(ProductType, description="The metadata associated with this Bundle which HumbleBundle calls a Product")
    gamekey= String(description="A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'")
    uid= String(description="A unique identifier for this Bundle used for several purposes in the HumbleBundle API.  Ex: 'X9GHPP9ABKS28'")
    all_coupon_data= List(Field(CouponType), description="A list of coupons which came with this bundle.")
    created= Date(description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'")
    # missed_credit= null  # TODO: what is the type of missed_credit ?  What is its purpose?
    subproducts= List(Field(SubProductType), description="A list of sub-products.  These are like downloadable games, books, etc.") # TODO: what is a sub product and how does it differ from a product?
    total_choices= Int(description="TODO: What does this field do?") # TODO: properly describe total choices
    tpkd_dict= Field(TpkdDictType, description="TODO: What a tpkd and what is a tpkd dict?") # TODO: Properly describe what a TPKD is and what this dict is for
    choices_remaining= Int(description="TODO: What are the 'choices' this refers to?") # TODO: what are choices?sd
    currency= String(description="A string representation of the currency, for example 'USD'")
    is_giftee= Boolean(description="Was this product given as a gift to the current user?")
    claimed= Boolean(description="Is this bundle claimed already by the current user?")
    total= Float(description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0 (TODO: how is this different from amount spent?)") # TODO: how is total and amount_spent different?
    path_ids= List(String(description="The path id"), description="The path ids TODO: what are Path IDs?  Are they the ID of this humble bundle for API calls?")


class BundleQuery(ObjectType):
    """The base query class for Bundle query resolvers, enabling remote fetching and local querying

    If the local database is empty, BundleQuery methods will attempt to update the
    local cache from the remote HumbleBundle library.  This remote fetching, parsing,
    and caching is handled by the ``Network`` service.
    """

    get_bundles = List(Field(Bundle), description("Returns a set of bundles filtered by various properties."))