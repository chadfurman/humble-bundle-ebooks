import time
import json
from bs4 import BeautifulSoup
from requests import Response

from typing import List
from dto.raw_order import RawOrderDTO
from utils.logger import log_debug

LIBRARY_PAGE_URL = 'https://www.humblebundle.com/home/library'
ORDER_ENDPOINT_URL = 'https://www.humblebundle.com/api/v1/order/{}?all_tpkds=true'
NETWORK_REQUEST_DELAY = .1


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
        log_debug('Network Service', 'Init with params', 'library_page_url: ' + library_page_url, 'order_endpoint_url: ' + order_endpoint_url)

    def fetch_raw_orders(self, session, csrf, ignore_sleep=False) -> List[RawOrderDTO]:
        '''
        .. function:: refresh_cache()

        Pull the latest data down from Humble Bundle.

        .. seealso:: :class: network_cache.NetworkLayer

        :return: None
        '''
        log_debug('Network Service', 'Fetching raw orders')
        raw_orders = []
        s = self.requests.session()
        s.cookies.set('_simpleauth_sess', session, domain='humblebundle.com')
        s.cookies.set('csrf_cookie', csrf, domain='humblebundle.com')
        response = s.get(self.library_page_url)
        log_debug('Network Service', 'Response Received')
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script', id='user-home-json-data')
        for script in scripts:
            log_debug('Network Service', 'Checking script tag for game keys')

            if 'gamekeys' in str(script):
                try:
                    gamekeys = json.loads(script.contents[0])['gamekeys']
                    log_debug('Network Service', 'Parsed gamekeys json')
                except:
                    continue
                print('found {} gamekeys'.format(len(gamekeys)))
                for gamekey in gamekeys:
                    # write
                    order_response = s.get(self.order_endpoint_url.format(gamekey))
                    log_debug('Network Service', 'Fetched order data for gamekey', 'gamekey: ' + gamekey)
                    raw_orders.append(self.order_response_to_raw_order_dto(order_response))
                    log_debug('Network Service', 'Added order response DTO to raw order return object')
                    if not ignore_sleep:
                        time.sleep(NETWORK_REQUEST_DELAY)
                    log_debug('Processed Gamekeys')
        return raw_orders

    def order_response_to_raw_order_dto(self, order_response: Response) -> RawOrderDTO:
        order = order_response.json()
        log_debug('Network Service', 'Converted raw order response to json')
        return RawOrderDTO(
            amount_spent=order.get('amount_spent'),
            product=order.get('product'),
            gamekey=order.get('gamekey'),
            uid=order.get('uid'),
            all_coupon_data=order.get('all_coupon_data'),
            created=order.get('created'),
            missed_credit=order.get('missed_credit'),
            subproducts=order.get('subproducts'),
            total_choices=order.get('total_choices'),
            tpkd_dict=order.get('tpkd_dict'),
            choices_remaining=order.get('choices_remaining'),
            currency=order.get('currency'),
            is_giftee=order.get('is_giftee'),
            claimed=order.get('claimed'),
            total=order.get('total'),
            path_ids=order.get('path_ids'),
        )


cache = NetworkService()