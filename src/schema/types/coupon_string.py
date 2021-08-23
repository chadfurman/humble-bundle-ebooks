from graphene import ObjectType, String

class CouponString(ObjectType):
    """Strings associated with a coupon"""
    terms=String(description="The terms of use for this coupon.  For example, 'Single use coupon. Coupon redeemable for 10% off one month of Humble Choice for new subscribers. This coupon may not be combined with other identical coupons in the same transaction, and may not be combined with other Humble Bundle coupons. Discount will be automatically applied at time of checkout. Coupon has no cash value. Void where prohibited or restricted by law. Coupon may not be reproduced, copied, purchased, traded or sold. Unauthorized transfer of coupon and internet distribution strictly prohibited.'")