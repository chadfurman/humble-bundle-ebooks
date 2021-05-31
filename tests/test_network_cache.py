import pickle

import pytest
from unittest.mock import patch, mock_open
from NetworkCache import cache, LIBRARY_PAGE_URL, ORDER_ENDPOINT_URL, NetworkLayer
import Credentials
from fixtures import example_library_page_response, example_order_response_for_order_2VnWY5u6C77Pc6yw, example_order_response_for_order_2cut2AGkahN7WqBK, example_order_response_for_order_2AZm2qDRvVUeqbKY


def make_request_response(code=None, text=None):
    return {
        'status_code': code,
        'text': text
    }


def new_request_get(self, *args, cookies=None, **kwargs):
    url = args[0]
    if cookies is None:
        return make_request_response(302, None)
    if url is ORDER_ENDPOINT_URL % '2VnWY5u6C77Pc6yw':
        return make_request_response(200, example_order_response_for_order_2VnWY5u6C77Pc6yw)
    if url is ORDER_ENDPOINT_URL % '2cut2AGkahN7WqBK':
        return make_request_response(200, example_order_response_for_order_2cut2AGkahN7WqBK)
    if url is ORDER_ENDPOINT_URL % '2AZm2qDRvVUeqbKY':
        return make_request_response(200, example_order_response_for_order_2AZm2qDRvVUeqbKY)
    if url is LIBRARY_PAGE_URL:
        return make_request_response(200, example_library_page_response)
    return None


def test_network_layer_get_library(self, example_library_page_response):
    with patch('NetworkCache.request.get') as mock_request_get:
        result = NetworkLayer.get_library()
        cookies = Credentials.get_cookies()
        assert result == example_library_page_response
        mock_request_get.assert_called_once_with(LIBRARY_PAGE_URL, cookies=cookies)


def test_network_layer_get_order(self, example_response_for_order_2VnWY5u6C77Pc6yw):
    order_id = '2VnWY5u6C77Pc6yw'
    with patch('NetworkCache.request.get', new=new_request_get) as mock_request_get:
        result = NetworkLayer.get_order(order=order_id)
        cookies = Credentials.get_cookies()
        assert result == example_response_for_order_2VnWY5u6C77Pc6yw
        mock_request_get.assert_called_once_with(ORDER_ENDPOINT_URL % order_id, cookies=cookies)


def test_refresh_cache(self, example_library_page_response):
    """
    should make a network request to the library page, parse out the gamekeys, and pull down the data for each bundle
    """
    with patch('NetworkCache.NetworkLayer.get_library') as mock_network_layer_get_library, patch('NetworkCache.NetworkLayer.get_order') as mock_network_layer_get_order:
        mock_network_layer_get_library.return_value = example_library_page_response
        cache.refresh()
        mock_network_layer_get_library.assert_called_once()
        mock_network_layer_get_order.assert_called_with(order_id='2VnWY5u6C77Pc6yw')
        mock_network_layer_get_order.assert_called_with(order_id='2cut2AGkahN7WqBK')
        mock_network_layer_get_order.assert_called_with(order_id='2AZm2qDRvVUeqbKY')


def test_get_from_cache(self, cache_fixture, example_library_page_response, example_response_for_order_2VnWY5u6C77Pc6yw):
    cache._cache = cache_fixture
    assert cache.get_library_response() == example_library_page_response
    assert cache.get_order('2VnWY5u6C77Pc6yw') == example_response_for_order_2VnWY5u6C77Pc6yw
    assert cache.get_order('asdfasdf123123') is None


def test_set_cache(self, example_library_page_response, example_response_for_order_2VnWY5u6C77Pc6yw):
    cache._cache = {}

    assert cache.get_library_response() is None
    cache.set_library_resposne(value=example_library_page_response)
    assert cache.get_library_response() is example_library_page_response

    order_id = '2VnWY5u6C77Pc6yw'
    assert cache.get_order(order=order_id) is None
    cache.set_order(order=order_id, value=example_response_for_order_2VnWY5u6C77Pc6yw)
    assert cache.get_library_response() is example_library_page_response


def test_load_cache(self, cache_fixture):
    with patch('NetworkCache.open', mock_open(readdata=pickle.dumps(cache_fixture))) as open_mock:
        cache._cache = None
        cache.load_cache()
        assert cache._cache == cache_fixture


def test_save_cache(self, cache_fixture):
    with patch('NetworkCache.open', mock_open()) as open_mock:
        cache._cache = None
        cache.save_cache()
        open_mock.write.assert_called_with(pickle.dumps(cache_fixture))
