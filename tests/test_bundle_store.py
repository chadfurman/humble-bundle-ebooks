import pytest
from fixtures import *

from app.bundle_store import BundleStore

def test_bundle_store_retrieves_all_bundle_ids(cache_fixture):
    bundle_ids = BundleStore(cache=cache_fixture).get_all_bundle_ids()
    assert bundle_ids == ["2cut2AGkahN7WqBK", "2AZm2qDRvVUeqbKY", "2VnWY5u6C77Pc6yw"]


def test_bundle_store_retrieves_data_by_bundle_id(cache_fixture, example_parsed_order_for_2VnWY5u6C77Pc6yw):
    bundle_id = "2VnWY5u6C77Pc6yw"
    bundle_data = BundleStore(cache=cache_fixture).get_bundle_data_by_bundle_id(bundle_id)
    assert bundle_data == example_parsed_order_for_2VnWY5u6C77Pc6yw


def test_bundle_store_retrieve_book_bundle_ids(cache_fixture, example_parsed_order_for_2VnWY5u6C77Pc6yw):
    book_bundles = BundleStore(cache=cache_fixture).retrieve_book_bundles()
    assert book_bundles == {
        "2VnWY5u6C77Pc6yw": example_parsed_order_for_2VnWY5u6C77Pc6yw
    }
