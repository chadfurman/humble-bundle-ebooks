from graphene import ObjectType, List, Field, String, Float, Date

class Bundle(ObjectType):
    """The GraphQL Bundle type represents a Bundle the authenticated user has in their library"""
    amount_spent= Float(description="The amount of currency that the user has spent on this bundle, represented as a float e.x. 25.0")
    product=Field(ProductType, description="The metadata associated with this Bundle which HumbleBundle calls a Product")
    gamekey= String(description="A gamekey, if any, for this bundle.  Not all bundles may have a gamekey.  ex: '2AZm2qDRsVUeqbKY'")
    uid= String(description="A unique identifier for this Bundle used for several purposes in the HumbleBundle API.  Ex: 'X9GHPP9ABKS28'")
    all_coupon_data= List(Field(CouponType), description="A list of coupons which came with this bundle.")
    created= Date(description="The date this Bundle was created.  Possibly the purchase date, but this may not be true.  Ex: '2019-12-06T06:58:10.488667'")
    missed_credit= null
    subproducts= []
    total_choices= 0
    tpkd_dict= TpkdDictType
    choices_remaining= 0
    currency= "USD"
    is_giftee= false
    claimed= true
    total= 25.0
    path_ids= ["48041806214594" ]
    '''

    name
    

class BundleQuery(ObjectType):
    """The base query class for Bundle query resolvers, enabling remote fetching and local querying

    If the local database is empty, BundleQuery methods will attempt to update the
    local cache from the remote HumbleBundle library.  This remote fetching, parsing,
    and caching is handled by the ``Network`` service.
    """

    get_bundles =