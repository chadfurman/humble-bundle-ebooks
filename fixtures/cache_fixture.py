import pytest

@pytest.fixture()
def cache_fixture(example_library_page_response, example_order_response_for_order_2cut2AGkahN7WqBK, example_order_response_for_order_2AZm2qDRvVUeqbKY, example_order_response_for_order_2VnWY5u6C77Pc6yw):
    return {
        'library_page_response': example_library_page_response,
        'orders': {
            '2cut2AGkahN7WqBK': example_order_response_for_order_2cut2AGkahN7WqBK,
            "2AZm2qDRvVUeqbKY": example_order_response_for_order_2AZm2qDRvVUeqbKY,
            "2VnWY5u6C77Pc6yw": example_order_response_for_order_2VnWY5u6C77Pc6yw,
        }
    }