import pytest
import os
import requests
import json
from services.network_service import NetworkService

@pytest.mark.skipif(reason="'E2E' not in os.environ")
def test_hb_request_response_via_network_service():
    try:
        session = os.environ['SESSION']
        csrf = os.environ['CSRF']
    except KeyError:
        raise KeyError('You must set both the SESSION and CSRF env vars when running this test')
    raw_orders = NetworkService(requests=requests).fetch_raw_orders(session=session, csrf=csrf)
    assert len(raw_orders) > 0, "You either have no bundles, or the API response / HTML has changed"
    assert raw_orders[0].product['machine_name'] is not None, "Either your bundle doesn't have a machine_name or the API response structure has changed"



