import json
from unittest.mock import Mock
from services.network_service import NetworkService, LIBRARY_PAGE_URL, ORDER_ENDPOINT_URL
import fixtures


class MockCookies(Mock):
    set = Mock()


class MockSession(Mock):
    cookies = MockCookies()
    get_calls = []
    fixtures = {}

    @classmethod
    def get(cls, url):
        cls.get_calls.append(url)
        if LIBRARY_PAGE_URL in url:
            return MockResponse(text=fixtures.example_library_page_response())
        if '2cut2AGkahN7WqBK' in url:
            return MockResponse(text=fixtures.example_order_response_for_order_2cut2AGkahN7WqBK())
        if '2AZm2qDRvVUeqbKY' in url:
            return MockResponse(text=fixtures.example_order_response_for_order_2AZm2qDRvVUeqbKY())
        if '2VnWY5u6C77Pc6yw' in url:
            return MockResponse(text=fixtures.example_order_response_for_order_2VnWY5u6C77Pc6yw())


class MockRequests(Mock):
    session = MockSession()


class MockResponse(Mock):
    text = None

    def __init__(self, text):
        super().__init__()
        self.text = text

    def json(self):
        return json.loads(self.text)




mock_requests = MockRequests()


def test_get_auth_key():
    mock_username = 'lotus'
    mock_password = 'lpwd'
    network_service = NetworkService(requests=mock_requests)
    session_key, csrf_key = network_service.get_auth_keys(username=mock_username, password=mock_password)


def test_fetch_raw_orders():
    mock_session_key = "mock_session_key"
    mock_csrf_key = "mock_csrf_key"
    network_service = NetworkService(requests=mock_requests)
    raw_orders = network_service.fetch_raw_orders(session=mock_session_key, csrf=mock_csrf_key)
    mock_requests.session.cookies.set.assert_any_call('_simpleauth_sess', mock_session_key, domain='humblebundle.com')
    mock_requests.session.cookies.set.assert_any_call('csrf_cookie', mock_csrf_key, domain='humblebundle.com')
    assert LIBRARY_PAGE_URL in mock_requests.session.get_calls
    assert ORDER_ENDPOINT_URL.format('2cut2AGkahN7WqBK') in mock_requests.session.get_calls
    assert ORDER_ENDPOINT_URL.format('2VnWY5u6C77Pc6yw') in mock_requests.session.get_calls
    assert ORDER_ENDPOINT_URL.format('2AZm2qDRvVUeqbKY') in mock_requests.session.get_calls
    assert len(raw_orders) == 3
    assert type(raw_orders[0]).__name__ == "RawOrderDTO"
    assert type(raw_orders[1]).__name__ == "RawOrderDTO"
    assert type(raw_orders[2]).__name__ == "RawOrderDTO"


def test_order_response_to_raw_order_dto():
    network_service = NetworkService(requests=mock_requests)
    order_response = MockResponse(text=fixtures.example_order_response_for_order_2cut2AGkahN7WqBK())
    order = order_response.json()
    raw_order = network_service.order_response_to_raw_order_dto(order_response)
    assert raw_order.product['category'] == order['product']['category']
    assert raw_order.product['machine_name'] == order['product']['machine_name']
    assert raw_order.product['empty_tpkds'] == order['product']['empty_tpkds']
    assert raw_order.product['post_purchase_text'] == order['product']['post_purchase_text']
    assert raw_order.product['human_name'] == order['product']['human_name']
    assert raw_order.product['partial_gift_enabled'] == order['product']['partial_gift_enabled']
    assert raw_order.gamekey == order['gamekey']
    assert raw_order.uid == order['uid']
    assert raw_order.all_coupon_data[0]['coupon_min_count'] == order['all_coupon_data'][0]['coupon_min_count']
    assert raw_order.all_coupon_data[0]['coupon_valid_products'] == order['all_coupon_data'][0]['coupon_valid_products']
    assert raw_order.all_coupon_data[0]['coupon_type'] == order['all_coupon_data'][0]['coupon_type']
    assert raw_order.all_coupon_data[0]['coupon_discount'] == order['all_coupon_data'][0]['coupon_discount']
    assert raw_order.all_coupon_data[0]['coupon_machine_name'] == order['all_coupon_data'][0]['coupon_machine_name']
    assert raw_order.all_coupon_data[0]['coupon_credit'] == order['all_coupon_data'][0]['coupon_credit']
    assert raw_order.all_coupon_data[0]['coupon_max_count'] == order['all_coupon_data'][0]['coupon_max_count']
    assert raw_order.all_coupon_data[0]['subscriptions'][0] == order['all_coupon_data'][0]['subscriptions'][0]
    assert raw_order.all_coupon_data[0]['coupon_exclude_monthly'] == order['all_coupon_data'][0]['coupon_exclude_monthly']
    assert raw_order.all_coupon_data[0]['coupon_expiration'] == order['all_coupon_data'][0]['coupon_expiration']
    assert raw_order.all_coupon_data[0]['coupon_price'] == order['all_coupon_data'][0]['coupon_price']
    assert raw_order.all_coupon_data[0]['coupon_stack'] == order['all_coupon_data'][0]['coupon_stack']
    assert raw_order.all_coupon_data[0]['coupon_key'] == order['all_coupon_data'][0]['coupon_key']
    assert raw_order.all_coupon_data[0]['coupon_storefront_link'] == order['all_coupon_data'][0]['coupon_storefront_link']
    assert raw_order.all_coupon_data[0]['storefront_product'] == order['all_coupon_data'][0]['storefront_product']
    assert raw_order.all_coupon_data[0]['strings']['terms'] == order['all_coupon_data'][0]['strings']['terms']
    assert raw_order.all_coupon_data[0]['coupon_status'] == order['all_coupon_data'][0]['coupon_status']
    assert raw_order.all_coupon_data[0]['coupon_human_name'] == order['all_coupon_data'][0]['coupon_human_name']

    assert raw_order.all_coupon_data[1]['coupon_min_count'] == order['all_coupon_data'][1]['coupon_min_count']
    assert raw_order.all_coupon_data[1]['coupon_valid_products'] == order['all_coupon_data'][1]['coupon_valid_products']
    assert raw_order.all_coupon_data[1]['coupon_type'] == order['all_coupon_data'][1]['coupon_type']
    assert raw_order.all_coupon_data[1]['coupon_discount'] == order['all_coupon_data'][1]['coupon_discount']
    assert raw_order.all_coupon_data[1]['coupon_machine_name'] == order['all_coupon_data'][1]['coupon_machine_name']
    assert raw_order.all_coupon_data[1]['coupon_credit'] == order['all_coupon_data'][1]['coupon_credit']
    assert raw_order.all_coupon_data[1]['coupon_max_count'] == order['all_coupon_data'][1]['coupon_max_count']
    assert raw_order.all_coupon_data[1]['coupon_exclude_monthly'] == order['all_coupon_data'][1]['coupon_exclude_monthly']
    assert raw_order.all_coupon_data[1]['coupon_expiration'] == order['all_coupon_data'][1]['coupon_expiration']
    assert raw_order.all_coupon_data[1]['coupon_price'] == order['all_coupon_data'][1]['coupon_price']
    assert raw_order.all_coupon_data[1]['coupon_stack'] == order['all_coupon_data'][1]['coupon_stack']
    assert raw_order.all_coupon_data[1]['coupon_key'] == order['all_coupon_data'][1]['coupon_key']
    assert raw_order.all_coupon_data[1]['coupon_storefront_link'] == order['all_coupon_data'][1]['coupon_storefront_link']
    assert raw_order.all_coupon_data[1]['storefront_product'] == order['all_coupon_data'][1]['storefront_product']
    assert raw_order.all_coupon_data[1]['strings'] == order['all_coupon_data'][1]['strings']
    assert raw_order.all_coupon_data[1]['coupon_status'] == order['all_coupon_data'][1]['coupon_status']
    assert raw_order.all_coupon_data[1]['coupon_human_name'] == order['all_coupon_data'][1]['coupon_human_name']
    assert raw_order.created == order['created']
    assert raw_order.missed_credit == order['missed_credit']
    assert raw_order.subproducts == order['subproducts']
    assert raw_order.total_choices == order['total_choices']
    assert raw_order.tpkd_dict == order['tpkd_dict']
    assert raw_order.choices_remaining == order['choices_remaining']
    assert raw_order.currency == order['currency']
    assert raw_order.is_giftee == order['is_giftee']
    assert raw_order.claimed == order['claimed']
    assert raw_order.total == order['total']
    assert raw_order.path_ids == order['path_ids']
