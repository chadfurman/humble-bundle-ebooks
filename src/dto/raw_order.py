from attr import define, field


@define
class RawOrderDTO:
    amount_spent = field()
    product = field()
    gamekey = field()
    uid = field()
    all_coupon_data = field()
    created = field()
    missed_credit = field()
    subproducts = field()
    total_choices = field()
    tpkd_dict = field()
    choices_remaining = field()
    currency = field()
    is_giftee = field()
    claimed = field()
    total = field()
    path_ids = field()