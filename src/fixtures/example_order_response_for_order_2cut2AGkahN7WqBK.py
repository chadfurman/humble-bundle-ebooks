import pytest

@pytest.fixture
def example_order_response_for_order_2cut2AGkahN7WqBK():
    return '''HTTP/2 200 OK
Cache-Control: no-cache
Content-Type: application/json; charset=utf-8
Set-Cookie: _simpleauth_sess=eyJ1c2VyX2lkIjo1OTU5OTEyOTY5NjAxMDI0LCJpZCI6InRWZE9HVzE4RWMiLCJhdXRoX3RpbWUiOjE2MjIzMzQ4NTd9|1622334943|7d2106a858df0ceff982070f8ec9283efdabab5e; Domain=.humblebundle.com; Max-Age=15552000; Path=/; expires=Fri, 26-Nov-2021 00:35:43 GMT; secure; HttpOnly
X-Cloud-Trace-Context: 202af53d2106c7a01d9694efd4592435
Vary: Accept-Encoding
Date: Sun, 30 May 2021 00:35:43 GMT
Server: Google Frontend
Content-Length: 22769
Expires: Sun, 30 May 2021 00:35:43 GMT

{
"amount_spent":15.0,
"product":{
"category":"bundle",
"machine_name":"hotdate_bundle",
"empty_tpkds":{},
"post_purchase_text":"",
"human_name":"Humble Hot Date Bundle",
"partial_gift_enabled":true
},
"gamekey":"2cut2AGkahN7WqBK",
"uid":"XA83BF1WH3HWK",
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
"coupon_key":4961402174177280,
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
"nationalparkgirls_storefront"
],
"coupon_type":"discount-percentage",
"coupon_discount":20.0,
"coupon_machine_name":"20percentoff_nationalparkgirls_hotdate_bundle",
"coupon_credit":null,
"coupon_max_count":1,
"coupon_exclude_monthly":false,
"coupon_expiration":"2019-04-23T18:00:00+00:00",
"coupon_price":null,
"coupon_stack":false,
"coupon_key":6616404034715648,
"coupon_storefront_link":"/store/national-park-girls",
"storefront_product":{
"machine_name":"nationalparkgirls_storefront",
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
"human_url":"national-park-girls",
"currency":"USD",
"discount_price|money":{
"currency":"USD",
"amount":3.99
},
"icon":"https://hb.imgix.net/0f0960a7d1515ab495cc91746f71b06f9c6c34ac.jpeg?auto=compress,format&fit=crop&h=64&w=103&s=487648d7ee673b3edb9e4eb4ed540a51"
},
"strings":{},
"coupon_status":"expired",
"coupon_human_name":"20% off National Park Girls"
},
{
"coupon_min_count":1,
"coupon_valid_products":[
"heartofthewoods_storefront"
],
"coupon_type":"discount-percentage",
"coupon_discount":20.0,
"coupon_machine_name":"20percentoff_heartofthewoods_hotdate_bundle",
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
"icon":"https://hb.imgix.net/6fb8ee959cde30d84fdd6e40a3aeaf9e6c542892.jpg?auto=compress,format&fit=crop&h=64&w=103&s=98822190c2ac80ebb990c08ce2fd7e06"
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
"machine_name":"highwayblossoms",
"url":"https://sekaiproject.com/",
"downloads":[
{
"machine_name":"highwayblossoms_windows",
"platform":"windows",
"download_struct":[
{
"sha1":"38c6e8afe3f2e74569cc24845ca29cf6b218603e",
"name":"Download",
"url":{
"web":"https://dl.humble.com/highwayblossoms_windows.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=ffaa585c216de0aadc8a66c6b8a5efce",
"bittorrent":"https://dl.humble.com/torrents/highwayblossoms_windows.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=c01d43b38331497587fb36033a27ebd7"
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
"machine_name":"highwayblossoms_mac",
"platform":"mac",
"download_struct":[
{
"sha1":"56b3dc4e25bbc260d633d95251964dabeef158b4",
"name":"Download",
"url":{
"web":"https://dl.humble.com/highwayblossoms_mac.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=3f96683e9e0119ee8a4519c37a3fda36",
"bittorrent":"https://dl.humble.com/torrents/highwayblossoms_mac.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=e075065e7dd8e5083f21ee102dfe6fcb"
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
"machine_name":"highwayblossoms_linux",
"platform":"linux",
"download_struct":[
{
"uploaded_at":"2019-03-26T21:28:00.117829",
"name":"Download",
"url":{
"web":"https://dl.humble.com/highway_blossoms_linux.bz2?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=6ba4ac147f8d421eb8b680720aea6caa",
"bittorrent":"https://dl.humble.com/torrents/highway_blossoms_linux.bz2.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=f09fac1ec18c4e006bd70a7106e95cad"
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
"human_name":"Sekai Project",
"machine_name":"sekaiproject"
},
"human_name":"Highway Blossoms",
"custom_download_page_box_css":null,
"custom_download_page_box_html":"",
"icon":"https://hb.imgix.net/b0e26dc6f3fcae4991d7f795deef34562a28f2c2.png?auto=compress,format&s=0f97f01241b1d40b18e548b06f13a50f"
},
{
"machine_name":"creatureromances_kokonoekokoro",
"url":"https://sekaiproject.com/",
"downloads":[
{
"machine_name":"creatureromances_kokonoekokoro_windows",
"platform":"windows",
"download_struct":[
{
"sha1":"aa73164b47c1167a87c819ffb344bfd60055ec85",
"name":"Download",
"url":{
"web":"https://dl.humble.com/creatureromances_kokonoekokoro_windows.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=bbcb21c9f30c32b8a32cd9733a2bacd7",
"bittorrent":"https://dl.humble.com/torrents/creatureromances_kokonoekokoro_windows.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=d1ea57c7f877547ee698384c77ef1a2f"
},
"human_size":"190.2 MB",
"file_size":199488579,
"small":0,
"md5":"ba8cd9c1a8b3e7d2b6668d8e8960d2eb"
}
],
"options_dict":{},
"download_identifier":"",
"android_app_only":false,
"download_version_number":null
},
{
"machine_name":"creatureromances_kokonoekokoro_mac",
"platform":"mac",
"download_struct":[
{
"sha1":"3804ea09a5cfeb100a7bb6a4f74dca188d28a086",
"name":"Download",
"url":{
"web":"https://dl.humble.com/creatureromances_kokonoekokoro_mac.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=5673af963e759a96d3affd0fd6edb2c9",
"bittorrent":"https://dl.humble.com/torrents/creatureromances_kokonoekokoro_mac.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=1a41b58eff4b55ccfb87f8e8c278f3f9"
},
"human_size":"195.3 MB",
"file_size":204805030,
"small":0,
"md5":"fcabc181a4aee473024f2fdf744f1a78"
}
],
"options_dict":{},
"download_identifier":"",
"android_app_only":false,
"download_version_number":null
},
{
"machine_name":"creatureromances_kokonoekokoro_linux",
"platform":"linux",
"download_struct":[
{
"sha1":"8c8e2f05b9a04c833d1fe051e82cfccbcac3bcbf",
"name":"Download",
"url":{
"web":"https://dl.humble.com/creatureromances_kokonoekokoro_linux.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=946ab9f40844bf9d9dcf84aaea520604",
"bittorrent":"https://dl.humble.com/torrents/creatureromances_kokonoekokoro_linux.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=f74835441bc2e3fbdba26409d4bace69"
},
"human_size":"209.1 MB",
"file_size":219261534,
"small":0,
"md5":"a5686187e7d887a8db6aa9ce491f4ea8"
}
],
"options_dict":{},
"download_identifier":"",
"android_app_only":false,
"download_version_number":null
}
],
"library_family_name":null,
"payee":{
"human_name":"Sekai Project",
"machine_name":"sekaiproject"
},
"human_name":"Creature Romances: Kokonoe Kokoro",
"custom_download_page_box_css":null,
"custom_download_page_box_html":null,
"icon":"https://hb.imgix.net/f6f62bfa5fca604cdf1c34671c74156311b07d99.png?auto=compress,format&s=bd1d07eb195576237e98e69b28061039"
},
{
"machine_name":"gsenjounomaou_thedevilongstring",
"url":"https://sekaiproject.com/",
"downloads":[
{
"machine_name":"gsenjounomaou_thedevilongstring_windows",
"platform":"windows",
"download_struct":[
{
"sha1":"690b765e87b80adfabbce20bc703ef7b078c619f",
"name":"Download",
"url":{
"web":"https://dl.humble.com/gsenjounomaou_thedevilongstring_windows.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=188559e189ba6fe8fa6e4b3dac3faf63",
"bittorrent":"https://dl.humble.com/torrents/gsenjounomaou_thedevilongstring_windows.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=baa22b8ef3d438c504d93dc856274367"
},
"human_size":"1.6 GB",
"file_size":1761050116,
"small":0,
"md5":"5a3056dd6b93198bbc6d8897ffaabd2a"
}
],
"options_dict":{},
"download_identifier":"",
"android_app_only":false,
"download_version_number":null
}
],
"library_family_name":null,
"payee":{
"human_name":"Sekai Project",
"machine_name":"sekaiproject"
},
"human_name":"G-senjou no Maou - The Devil on G-String Voiced Edition",
"custom_download_page_box_css":null,
"custom_download_page_box_html":null,
"icon":"https://hb.imgix.net/c4c066a5876c9a61f28ecc7fcef648ca3cfe4689.png?auto=compress,format&s=beeedcfe281d8b32df6d634c53f6f372"
},
{
"machine_name":"ladykiller_in_a_bind_ShxAc",
"url":"http://ladykillerinabind.com",
"downloads":[
{
"machine_name":"ladykiller_in_a_bind_shxac_windows_tM5tX",
"platform":"windows",
"download_struct":[
{
"uploaded_at":"2017-06-27T00:41:43.473210",
"name":"Download",
"url":{
"web":"https://dl.humble.com/christinelove/ladykiller-win_v1.1.4.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=70e9a1e7d069d1adb14ae3d0d87ab9eb",
"bittorrent":"https://dl.humble.com/torrents/christinelove/ladykiller-win_v1.1.4.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=dc83f8b7b350ddbfae092b88ae5a445d"
},
"timestamp":1498524304,
"human_size":"512.9 MB",
"file_size":537850792,
"small":0,
"md5":"7dc7a53e883ea9ceb8ccab561d90b13d"
}
],
"options_dict":{},
"download_identifier":null,
"android_app_only":false,
"download_version_number":null
},
{
"machine_name":"ladykiller_in_a_bind_shxac_linux_LU2C5",
"platform":"linux",
"download_struct":[
{
"uploaded_at":"2017-06-27T00:21:03.758390",
"name":"Download",
"url":{
"web":"https://dl.humble.com/christinelove/ladykiller-linux-v1.1.4.tar.bz2?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=367986ac2563c35c8de45f05a37976f4",
"bittorrent":"https://dl.humble.com/torrents/christinelove/ladykiller-linux-v1.1.4.tar.bz2.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=80a06e202e1c2075705ced17d3ab38eb"
},
"timestamp":1498523043,
"human_size":"510.4 MB",
"file_size":535195344,
"small":0,
"md5":"d68a9309b460f75f20fc1fc1c06c0749"
}
],
"options_dict":{},
"download_identifier":null,
"android_app_only":false,
"download_version_number":null
},
{
"machine_name":"ladykiller_in_a_bind_shxac_mac_b7REC",
"platform":"mac",
"download_struct":[
{
"uploaded_at":"2017-06-27T01:02:42.783480",
"name":"Download",
"url":{
"web":"https://dl.humble.com/christinelove/Ladykiller_in_a_Bind_v1.1.4.dmg?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=a7b25bcb0707a9ca8f1098e887cba089",
"bittorrent":"https://dl.humble.com/torrents/christinelove/Ladykiller_in_a_Bind_v1.1.4.dmg.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=fb710de58578b166c51528fc26508cd2"
},
"timestamp":1498525556,
"human_size":"507.1 MB",
"file_size":531741447,
"small":0,
"md5":"c4beb7f9a1472d041eb8adf3d578d276"
}
],
"options_dict":{},
"download_identifier":null,
"android_app_only":false,
"download_version_number":null
}
],
"library_family_name":null,
"payee":{
"human_name":"Christine Love",
"machine_name":"christinelove"
},
"human_name":"Ladykiller in a Bind",
"custom_download_page_box_css":null,
"custom_download_page_box_html":null,
"icon":"https://hb.imgix.net/c72715c9593f08c0f026318c1effdb3b27e04bb6.png?auto=compress,format&s=28960ee13d5d3a1ff458a042c7348fab"
},
{
"machine_name":"clannad",
"url":"https://sekaiproject.com/",
"downloads":[
{
"machine_name":"clannad_windows",
"platform":"windows",
"download_struct":[
{
"sha1":"ec78feddab68c9a68871bc401ac82afabb2ffb90",
"name":"Download",
"url":{
"web":"https://dl.humble.com/clannad_windows.zip?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=05f8e2dddd22f7689dddc838edb62003",
"bittorrent":"https://dl.humble.com/torrents/clannad_windows.zip.torrent?gamekey=2cut2AGkahN7WqBK&ttl=1622421342&t=734401b44227c83b08453e6072c9fc80"
},
"human_size":"5.1 GB",
"file_size":5442480707,
"small":0,
"md5":"b55cad6acb833a186406f49711d6b8f1"
}
],
"options_dict":{},
"download_identifier":"",
"android_app_only":false,
"download_version_number":null
}
],
"library_family_name":null,
"payee":{
"human_name":"Sekai Project",
"machine_name":"sekaiproject"
},
"human_name":"CLANNAD",
"custom_download_page_box_css":null,
"custom_download_page_box_html":null,
"icon":"https://hb.imgix.net/d3c74d838bca036d50a23536fdf86c813130802c.png?auto=compress,format&s=ceb2d9b704d8d0ae3903533743ed8524"
}
],
"total_choices":0,
"tpkd_dict":{
"all_tpks":[
{
"machine_name":"creatureromances_kokonoekokoro_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"Creature Romances: Kokonoe Kokoro",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"highwayblossoms_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
{
"machine_name":"justdeserts_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":488660,
"human_name":"Just Deserts",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":false,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"ladykillerinabind_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"Ladykiller in a Bind",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"purrfectdate_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"Purrfect Date - Visual Novel/Dating Simulator",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"genitaljousting_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"Genital Jousting",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"gsenjounomaou_thedevilongstring_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"G-senjou no Maou - The Devil on G-String Voiced Edition",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"sunrideracademy_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":340730,
"human_name":"Sunrider Academy",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"sunrider_liberationday_themesong_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"Sunrider: Liberation Day - Theme Song",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"sunrider_liberationday_captainsedition_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":438130,
"human_name":"Sunrider: Liberation Day - Captain's Edition",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
},
{
"machine_name":"clannad_bundle_steam",
"gamekey":"2cut2AGkahN7WqBK",
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
"steam_app_id":null,
"human_name":"CLANNAD",
"preinstruction_text":"Copy this key into the Steam client, or click Redeem to redeem in-browser.",
"auto_expand":true,
"is_expired":false,
"class":"steambutton",
"keyindex":0,
"disclaimer":"Steam will not provide extra giftable copies of games you already own."
}
]
},
"choices_remaining":0,
"currency":"USD",
"is_giftee":false,
"claimed":true,
"total":15.0,
"path_ids":[
"5921558017998848"
]
}'''