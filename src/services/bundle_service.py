from network_service import NetworkService

class BundleService(object):
    """
    This is where the data for your Humble Bundle library can be accessed

    Supports GraphQL style interfacing.  All methods are resolvers in the schema.
    """
    def __init__(self, cache: NetworkService) -> None:
        self.cache = cache

    def get_all_bundle_ids(self) -> list:
        """
        Returns a list of bundle IDs stored in the local `cache` which is an instance of :class:`network_cache.NetworkCache`

        Can be used if you need to iterate over all your different bundles, for example to query for their data

        :return: List of bundle IDs
        :rtype: list
        """
        return list(self.cache.get("orders").keys())

    def get_all_bundles_with_metadata(self) -> list:
        """
        Returns a dictionary whose keys are bundle IDs and whose values are also dictionaries.

        Each bundle ID holds a dictionary containing all data returned from the network call for the bundle.

        An example dictionary could look like this::

            {
                "amount_spent":15.0,
                "product":{
                    "category":"bundle",
                    "machine_name":"my_bundle",
                    "empty_tpkds":{},
                    "post_purchase_text":"",
                    "human_name":"My Bundle",
                    "partial_gift_enabled":true
                },
                "gamekey":"2idt2IDidD7IdBi",
                "uid":"IDIDIDIDIDIDI",
                "all_coupon_data":[
                    {
                        "coupon_min_count":null,
                        "coupon_valid_products":[],
                        "coupon_type":"relative-discount-plan",
                        "coupon_discount":10.0,
                        "coupon_machine_name":"humblemonthly_10percentoff_bundle",
                        "coupon_credit":null,
                        "coupon_max_count":null,
                        "subscriptions":[
                            "humble_monthly"
                        ],
                        "coupon_exclude_monthly":false,
                        "coupon_expiration":"2019-06-07T17:00:00+00:00",
                        "coupon_price":null,
                        "coupon_stack":false,
                        "coupon_key":4961411114177280,
                        "coupon_storefront_link":"/subscription",
                        "storefront_product":null,
                        "strings":{
                            "terms":"Single use coupon. Coupon redeemable for 10% off one month of Humble Choice for new subscribers. This coupon may not be combined with other identical coupons in the same transaction, and may not be combined with other Humble Bundle coupons. Discount will be automatically applied at time of checkout. Coupon has no cash value. Void where prohibited or restricted by law. Coupon may not be reproduced, copied, purchased, traded or sold. Unauthorized transfer of coupon and internet distribution strictly prohibited."
                        },
                        "coupon_status":"expired",
                        "coupon_human_name":"10% off your first month of Humble Choice"
                    },
                    {
                        "coupon_min_count":1,
                        "coupon_valid_products":[
                            "nationalpark_storefront"
                        ],
                        "coupon_type":"discount-percentage",
                        "coupon_discount":20.0,
                        "coupon_machine_name":"20percentoff_nationalpark_bundle",
                        "coupon_credit":null,
                        "coupon_max_count":1,
                        "coupon_exclude_monthly":false,
                        "coupon_expiration":"2019-04-23T18:00:00+00:00",
                        "coupon_price":null,
                        "coupon_stack":false,
                        "coupon_key":6616111111111118,
                        "coupon_storefront_link":"/store/national-park",
                        "storefront_product":{
                        "machine_name":"nationalpark_storefront",
                        "platform_icon_dict":{
                        "steam":{
                        "available":[
                        "windows",
                        "mac",
                        "linux"
                        ],
                        "unavailable":[]
                        }
                        },
                        "human_url":"national-park",
                        "currency":"USD",
                        "discount_price|money":{
                        "currency":"USD",
                        "amount":3.99
                        },
                        "icon":"https://hb.imgix.net/123.jpeg?..."
                        },
                        "strings":{},
                        "coupon_status":"expired",
                        "coupon_human_name":"20% off National Park"
                    },
                    {
                        "coupon_min_count":1,
                        "coupon_valid_products":[
                                "heartofthewoods_storefront"
                            ],
                        "coupon_type":"discount-percentage",
                        "coupon_discount":20.0,
                        "coupon_machine_name":"20percentoff_heartofthewoods_bundle",
                        "coupon_credit":null,
                        "coupon_max_count":1,
                        "coupon_exclude_monthly":false,
                        "coupon_expiration":"2019-04-23T18:00:00+00:00",
                        "coupon_price":null,
                        "coupon_stack":false,
                        "coupon_key":4955766036234240,
                        "coupon_storefront_link":"/store/heart-of-the-woods",
                        "storefront_product":{
                            "machine_name":"heartofthewoods_storefront",
                            "platform_icon_dict":{
                                "steam":{
                                    "available":[
                                        "windows",
                                        "mac",
                                        "linux"
                                    ],
                                    "unavailable":[]
                                }
                            },
                            "human_url":"heart-of-the-woods",
                            "currency":"USD",
                            "discount_price|money":{
                                "currency":"USD",
                                "amount":11.99
                            },
                            "icon":"https://hb.imgix.net/....jpg?..."
                        },
                        "strings":{},
                        "coupon_status":"expired",
                        "coupon_human_name":"20% off Heart of the Woods"
                    }
                ],
                "created":"2019-04-07T22:46:50.938487",
                "missed_credit":null,
                "subproducts":[
                    {
                        "machine_name":"blossoms",
                        "url":"https://sproject.com/",
                        "downloads":[
                            {
                                "machine_name":"blossoms_windows",
                                "platform":"windows",
                                "download_struct":[
                                    {
                                        "sha1":"38c6e8afe3f2e74569cc24845ca29cf6b218603e",
                                        "name":"Download",
                                        "url":{
                                            "web":"https://dl.humble.com/...",
                                            "bittorrent":"https://dl.humble.com/torrents/..."
                                        },
                                        "human_size":"677.1 MB",
                                        "file_size":709940417,
                                        "small":0,
                                        "md5":"dedcc64717a853644d54cfabe4413d06"
                                    }
                                ],
                                "options_dict":{},
                                "download_identifier":"",
                                "android_app_only":false,
                                "download_version_number":null
                            },
                            {
                                "machine_name":"blossoms_mac",
                                "platform":"mac",
                                "download_struct":[
                                    {
                                        "sha1":"56b3dc4e25bbc260d633d95251964dabeef158b4",
                                        "name":"Download",
                                        "url":{
                                            "web":"https://dl.humble.com/...",
                                            "bittorrent":"https://dl.humble.com/torrents/..."
                                        },
                                        "human_size":"676 MB",
                                        "file_size":708870408,
                                        "small":0,
                                        "md5":"40f45258398694b458ed7481a8f876e0"
                                    }
                                ],
                                "options_dict":{},
                                "download_identifier":"",
                                "android_app_only":false,
                                "download_version_number":null
                            },
                            {
                                "machine_name":"blossoms_linux",
                                "platform":"linux",
                                "download_struct":[
                                    {
                                        "uploaded_at":"2019-03-26T21:28:00.117829",
                                        "name":"Download",
                                        "url":{
                                            "web":"https://dl.humble.com/...",
                                            "bittorrent":"https://dl.humble.com/torrents/..."
                                        },
                                        "human_size":"679.3 MB",
                                        "file_size":712316687,
                                        "small":0,
                                        "md5":"c1fd03437e15903792982f1b3e5d3fb3"
                                    }
                                ],
                                "options_dict":{},
                                "download_identifier":null,
                                "android_app_only":false,
                                "download_version_number":null
                            }
                        ],
                        "library_family_name":"",
                        "payee":{
                            "human_name":"S Project",
                            "machine_name":"s_project"
                        },
                        "human_name":"Blossoms",
                        "custom_download_page_box_css":null,
                        "custom_download_page_box_html":"",
                        "icon":"https://hb.imgix.net/123.png?..."
                    },
                ],
                "total_choices":0,
                "tpkd_dict":{
                    "all_tpks":[
                        {
                            "machine_name":"blossoms_bundle_steam",
                            "gamekey":"...",
                            "exclusive_countries":[],
                            "num_days_until_expired":-1,
                            "disallowed_countries":[],
                            "show_custom_instructions_in_user_libraries":false,
                            "key_type":"steam",
                            "visible":true,
                            "sold_out":false,
                            "instructions_html":"<a href='https://support.humblebundle.com/hc/articles/204008710-How-To-Redeem-Steam-Keys' target='_blank'>Steam Instructions</a>",
                            "display_separately":false,
                            "direct_redeem":false,
                            "key_type_human_name":"Steam",
                            "steam_app_id":451760,
                            "human_name":"Highway Blossoms",
                            "preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
                            "auto_expand":true,
                            "is_expired":false,
                            "class":"steambutton",
                            "keyindex":0,
                            "disclaimer":"Steam will not provide extra giftable copies of games you already own."
                        },
                    ]
                },
                "choices_remaining":0,
                "currency":"USD",
                "is_giftee":false,
                "claimed":true,
                "total":15.0,
                "path_ids":[
                    "5921558011118848"
                ]
            }
        :return:
        """
        pass


    def get_bundle_by_id(self, bundle_id: str):
        pass


    def search_bundles(self, search_params):
        """
        Quite possibly the most useful method.
        All search params that take a string support fuzzy matching with Levenshtein Distance.
        All search params that take an enum support lists with comma-separated values

        Search params:
        * product name
        * operating system (game / software only)
            * macintosh
            * windows
            * linux
        * format (ebook only)
            * epub
            * pdf
            * mobi
            * other
        * type
            * game
            * ebook
            * software
            * other

        :param search_options:
        :return: list of matching Bundles
        """
        pass
