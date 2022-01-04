import os
import json
from bs4 import BeautifulSoup
from utils.logger import log_error
from sqlitedict import SqliteDict
from typing import List
from dto.raw_order import RawOrderDTO

LIBRARY_PAGE_URL = 'https://www.humblebundle.com/home/library'
ORDER_ENDPOINT_URL = 'https://www.humblebundle.com/api/v1/order/{}?all_tpkds=true'
#SESSION_KEY = '' # pull this from the browser console
#CSRF_COOKIE = '' # pull this from the browser console


class NetworkLayer(object):
    """
    A helper utility for working directly with the Humble Bundle API

    Initialize it with credentials and ask it to retrieve your data like so::
        credentials = Credentials(username="me@example.org", password="P@s5w0rd123!")
        network_layer = NetworkLayer(credentials)
        raw_humble_bundle_data = network_layer.retrieve_library()

    .. note::

        You likely don't want to work with this layer directly.
        Instead, consider using :class: NetworkCache()
    """
    pass


# TODO: Convert NetworkCache to use SQLiteDict
class NetworkService(object):
    requests = None

    def __init__(self, requests=None, library_page_url=LIBRARY_PAGE_URL, order_endpoint_url=ORDER_ENDPOINT_URL):
        self.requests = requests
        self.library_page_url = library_page_url
        self.order_endpoint_url = order_endpoint_url

    def fetch_raw_orders(self, session_key, csrf_key) -> List[RawOrderDTO]:
        '''
        .. function:: refresh_cache()

        Pull the latest data down from Humble Bundle.

        .. seealso:: :class: network_cache.NetworkLayer

        :return: None
        '''
        raw_orders = []
        s = self.requests.session()
        s.cookies.set('_simpleauth_sess', session_key, domain='humblebundle.com')
        s.cookies.set('csrf_cookie', csrf_key, domain='humblebundle.com')
        response = s.get(self.library_page_url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        for script in scripts:
            if 'gamekeys' in str(script):
                #print(script.contents[0])
                gamekeys = json.loads(script.contents[0])['gamekeys']
                for gamekey in gamekeys:
                    # write
                    order_response = s.get(self.order_endpoint_url.format(gamekey))
                    raw_orders.append(self.order_response_to_raw_order_dto(order_response))
        return raw_orders

    def order_response_to_raw_order_dto(self, order_response):
        order = order_response.json()
        return RawOrderDTO(
            amount_spent=order['amount_spent'],
            product=order['product'],
            gamekey=order['gamekey'],
            uid=order['uid'],
            all_coupon_data=order['all_coupon_data'],
            created=order['created'],
            missed_credit=order['missed_credit'],
            subproducts=order['subproducts'],
            total_choices=order['total_choices'],
            tpkd_dict=order['tpkd_dict'],
            choices_remaining=order['choices_remaining'],
            currency=order['currency'],
            is_giftee=order['is_giftee'],
            claimed=order['claimed'],
            total=order['total'],
            path_ids=order['path_ids'],
        )

cache = NetworkService()