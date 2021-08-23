from graphene import String, ObjectType, Float, List, Boolean, Date, Field
from .coupon_string import CouponString

class Coupon(ObjectType):
    """A coupon for discounts on products"""
    coupon_min_count=String(description="TODO: What is the format of this?  What is its purpose?")
    coupon_valid_products=List(String(description="List of valid products. TODO: What is the format of this?"))
    coupon_type=String(description="The type of this coupon.  For example, 'relative-discount-plan'. TODO: Make this an enum")
    coupon_discount=Float(description="The amount of the discount.  For example 10.0")
    coupon_machine_name=String(description="The machine readable name of this coupon.  For example, 'humblemonthly_10percentoff_bundle'")
    coupon_credit=String(description="TODO: What is this?")
    coupon_max_count=String(description="TODO: What is this?")
    subscriptions=List(String(), description="The subscriptions associated with this coupon.  For example, 'humble_monthly'")
    coupon_exclude_monthly=Boolean(description="A flag indicating whether or not this coupon is excluded for monthly subscriptions TODO: What is this?")
    coupon_expiration=Date(description="The date of this coupon's expiration, for example '2020-01-03T18:00:00+00:00'")
    coupon_price=String(description="The price of this coupon. TODO: verify")
    coupon_stack=String(description="Whether or not this coupon stacks. TODO: verify")
    coupon_key=String(description="The key for this coupon.  For example '6672880223977472'")
    coupon_storefront_link=String(description="The path to access this coupon.  For example '/subscription'")
    storefront_product=String(description="TODO: what is this?")
    strings=Field(CouponString, description="A set of strings associated with this coupon.  Check CouponString for more information.")
    coupon_status=String(description="The status of this coupon.  For example, 'expired'. TODO: Make this an enum")
    coupon_human_name=String(description="The Human Readable name for this coupon.  For example, '10% off your first month of Humble Choice'")