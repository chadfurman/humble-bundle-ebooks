import pytest
from . import bundle
from attr import asdict


def test_bundle_is_attr():
    MOCK_BUNDLE_ID = "MOCK_ID"
    MOCK_BUNDLE_NAME = "Mock Bundle"
    b = bundle.Bundle(bundle_id=MOCK_BUNDLE_ID, bundle_name=MOCK_BUNDLE_NAME)
    b_dict = asdict(b)
    assert b.bundle_id == MOCK_BUNDLE_ID
    assert b.bundle_name == MOCK_BUNDLE_NAME
    assert b_dict['bundle_id'] == MOCK_BUNDLE_ID
    assert b_dict['bundle_name'] == MOCK_BUNDLE_NAME
    assert b_dict['amount_spent'] is None
