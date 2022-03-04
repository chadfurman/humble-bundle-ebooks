from unittest.mock import create_autospec, Mock
from typing import List
from repositories.bundle import BundleRepository
from services.bundle_service import BundleService

import pytest

from dto.raw_order import RawOrderDTO

MOCK_AMOUNT_SPENT = 25.0
MOCK_PRODUCT = {
    "category":"bundle",
    "machine_name":"2danimation_softwarebundle",
    "empty_tpkds":{},
    "post_purchase_text":"",
    "human_name":"Humble Software Bundle: 2D Animation",
    "partial_gift_enabled":True
}
MOCK_GAMEKEY = "2AZm2qDRvVUeqbKY"
MOCK_UID = "X9GHPP9ABKE28"
MOCK_ALL_COUPON_DATA = [
    {
        "coupon_min_count":None,
        "coupon_valid_products":[],
        "coupon_type":"relative-discount-plan",
        "coupon_discount":10.0,
        "coupon_machine_name":"humblemonthly_10percentoff_bundle",
        "coupon_credit":None,
        "coupon_max_count":None,
        "subscriptions":[
            "humble_monthly"
        ],
        "coupon_exclude_monthly":False,
        "coupon_expiration":"2020-01-03T18:00:00+00:00",
        "coupon_price":None,
        "coupon_stack":False,
        "coupon_key":6672880223977472,
        "coupon_storefront_link":"/subscription",
        "storefront_product":None,
        "strings":{
            "terms":"Single use coupon. Coupon redeemable for 10% off one month of Humble Choice for new subscribers. This coupon may not be combined with other identical coupons in the same transaction, and may not be combined with other Humble Bundle coupons. Discount will be automatically applied at time of checkout. Coupon has no cash value. Void where prohibited or restricted by law. Coupon may not be reproduced, copied, purchased, traded or sold. Unauthorized transfer of coupon and internet distribution strictly prohibited."
        },
        "coupon_status":"expired",
        "coupon_human_name":"10% off your first month of Humble Choice"
    }
]
MOCK_CREATED = "2019-12-06T06:58:10.488667"
MOCK_MISSED_CREDIT = None
MOCK_SUBPRODUCTS = []
MOCK_TOTAL_CHOICES = 0
MOCK_TPKD_DICT = {
    "all_tpks":[
        {
            "exclusive_countries":[],
            "machine_name":"2danimation_softwarebundle_bt1_reallusion",
            "gamekey":"2AZm2qDRvVUeqbKY",
            "custom_instructions_html":"<div class=\"instructions_html overgrowthspf_instruct\" style=\"text-align: center;\">\r\n\t<center>\r\n\t\t<p style=\"font-size: 15px\">\r\n\t\t\t <a href=\"https://support.humblebundle.com/hc/en-us/articles/360038790114\" target=\"_blank\">Redemption Instructions</a>.\r\n\t\t</p>\r\n\t</center>\r\n</div>",
            "disallowed_countries":[],
            "show_custom_instructions_in_user_libraries":False,
            "key_type":"generic",
            "visible":True,
            "sold_out":False,
            "display_separately":True,
            "direct_redeem":False,
            "key_type_human_name":"other",
            "keyindex":0,
            "human_name":"2D Animation $1 Tier",
            "auto_expand":True,
            "is_expired":False,
            "class":"genericbutton",
            "num_days_until_expired":-1
        },
        {
            "exclusive_countries":[],
            "machine_name":"2danimation_soft_bta_reallusion",
            "gamekey":"2AZm2qDRvVUeqbKY",
            "custom_instructions_html":"<div class=\"instructions_html overgrowthspf_instruct\" style=\"text-align: center;\">\r\n\t<center>\r\n\t\t<p style=\"font-size: 15px\">\r\n\t\t\t <a href=\"https://support.humblebundle.com/hc/en-us/articles/360038790114\" target=\"_blank\">Redemption Instructions</a>.\r\n\t\t</p>\r\n\t</center>\r\n</div>",
            "disallowed_countries":[],
            "show_custom_instructions_in_user_libraries":False,
            "key_type":"generic",
            "visible":True,
            "sold_out":False,
            "display_separately":True,
            "direct_redeem":False,
            "key_type_human_name":"other",
            "keyindex":0,
            "human_name":"2D Animation BTA Tier",
            "auto_expand":True,
            "is_expired":False,
            "class":"genericbutton",
            "num_days_until_expired":-1
        },
        {
            "exclusive_countries":[],
            "machine_name":"2danimation_soft_bt25_reallusion",
            "gamekey":"2AZm2qDRvVUeqbKY",
            "custom_instructions_html":"<div class=\"instructions_html overgrowthspf_instruct\" style=\"text-align: center;\">\r\n\t<center>\r\n\t\t<p style=\"font-size: 15px\">\r\n\t\t\t <a href=\"https://support.humblebundle.com/hc/en-us/articles/360038790114\" target=\"_blank\">Redemption Instructions</a>.\r\n\t\t</p>\r\n\t</center>\r\n</div>",
            "disallowed_countries":[],
            "show_custom_instructions_in_user_libraries":False,
            "key_type":"generic",
            "visible":True,
            "sold_out":False,
            "display_separately":True,
            "direct_redeem":False,
            "key_type_human_name":"other",
            "keyindex":0,
            "human_name":"2D Animation $25 Tier",
            "auto_expand":True,
            "is_expired":False,
            "class":"genericbutton",
            "num_days_until_expired":-1
        }
    ]
}
MOCK_CHOICES_REMAINING = 0
MOCK_CURRENCY = "USD"
MOCK_IS_GIFTEE = False
MOCK_CLAIMED = True
MOCK_TOTAL = 25.0
MOCK_PATH_IDS = [ "4804180621459456" ]


@pytest.fixture
def raw_order_factory():
    def factory(
        amount_spent = MOCK_AMOUNT_SPENT,
        product = None,
        gamekey = MOCK_GAMEKEY,
        uid = MOCK_UID,
        all_coupon_data = None,
        created = MOCK_CREATED,
        missed_credit = MOCK_MISSED_CREDIT,
        subproducts = None,
        total_choices = MOCK_TOTAL_CHOICES,
        tpkd_dict = None,
        choices_remaining = MOCK_CHOICES_REMAINING,
        currency = MOCK_CURRENCY,
        is_giftee = MOCK_IS_GIFTEE,
        claimed = MOCK_CLAIMED,
        total = MOCK_TOTAL,
        path_ids = None
    ) -> RawOrderDTO :
        product = product or MOCK_PRODUCT
        all_coupon_data = all_coupon_data or MOCK_ALL_COUPON_DATA
        subproducts = subproducts or MOCK_SUBPRODUCTS
        tpkd_dict = tpkd_dict or MOCK_TPKD_DICT
        path_ids = path_ids or MOCK_PATH_IDS

        return RawOrderDTO(
            amount_spent=amount_spent,
            product=product,
            gamekey=gamekey,
            uid=uid,
            all_coupon_data=all_coupon_data,
            created=created,
            missed_credit=missed_credit,
            subproducts=subproducts,
            total_choices=total_choices,
            tpkd_dict=tpkd_dict,
            choices_remaining=choices_remaining,
            currency=currency,
            is_giftee=is_giftee,
            claimed=claimed,
            total=total,
            path_ids=path_ids,
        )
    return factory

class MockNetworkService(object):
    calls = []
    raw_order_response = []

    def __init__(self, raw_order_response=None):
        for x in raw_order_response:
            self.raw_order_response.append(x)

    def fetch_raw_orders(self, session, csrf) -> List[RawOrderDTO]:
        self.calls.append(('fetch_library', session, csrf))
        return [RawOrderDTO(), RawOrderDTO()]


def test_retrieve_remote_bundles_with_credentials(raw_order_factory):
    mock_session_key = "MOCK_USER"
    mock_csrf_key = "MOCK_PASSWORD"
    raw_order_1 = raw_order_factory()
    mock_network_service = Mock()
    mock_network_service.fetch_raw_orders = lambda session, csrf: [raw_order_1] if session == mock_session_key and csrf == mock_csrf_key else None
    mock_bundle_repository = create_autospec(BundleRepository)
    mock_bundle_repository.create = Mock()
    service = BundleService(network_service=mock_network_service, bundle_repository=mock_bundle_repository)
    service.retrieve_remote_bundles_with_credentials(session=mock_session_key, csrf=mock_csrf_key)
    assert mock_bundle_repository.create.call_args_list[0].args[0].bundle_name == raw_order_1.product['human_name']