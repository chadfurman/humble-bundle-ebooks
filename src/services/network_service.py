import os
import requests
import json
from bs4 import BeautifulSoup
from utils.logger import log_error
from sqlitedict import SqliteDict

CACHE_FILENAME = os.path.join(os.path.dirname(__file__), 'cache')
LIBRARY_PAGE_URL = 'https://humblebundle.com/home/library'
ORDER_ENDPOINT_URL = 'https://humblebundle.com/api/v1/order/%s'
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
    _cache = None

    def __init__(self):
#        self.load_cache()
        pass

    def refresh_cache(self) -> None:
        '''
        .. function:: refresh_cache()

        Pull the latest data down from Humble Bundle.

        .. seealso:: :class: network_cache.NetworkLayer

        :return: None
        '''
        s = requests.session()
        s.cookies.set('_simpleauth_sess', SESSION_KEY, domain='humblebundle.com')
        s.cookies.set('csrf_cookie', CSRF_COOKIE, domain='humblebundle.com')
        #response = s.get('https://www.humblebundle.com/home/library?hmb_source=navbar')
        #content = open('./response.content.out', 'w+')
        content = open('./response.content.out', 'r+')
        #content.write(response.content.decode('utf-8'))
        html = content.read()
        soup = BeautifulSoup(html, 'html.parser')
        scripts = soup.find_all('script')
        print('trying...')
        for script in scripts:
            if 'gamekeys' in str(script):
                #print(script.contents[0])
                gamekeys = json.loads(script.contents[0])['gamekeys']
                key = gamekeys[0]
                #for key in gamekeys:
                print('requesting {}'.format(key))
                # write
                #order_response_content = open('./order_response_content.out', 'w+')
                #order_response = s.get("https://www.humblebundle.com/api/v1/order/{}?all_tpkds=true".format(key))
                #order_response_json = order_response.json()
                #print('writing ' + str(order_response_json))
                #json.dump(order_response_json, order_response_content)
                # read
                order_response_content = open('./order_response_content.out', 'r')
                order_response_json: dict = json.load(order_response_content)
                self.save_order(order_response_json)
                print(str(order_response_json))


        print("Done")

    def save_order(self, order_response_json: dict) -> bool:
        """Take in a dictionary representation of an order and write it to the db

        Args:
            order_response_json (dict): The dictionary representation of the order from a network request.
        Returns:
            (bool): True if the order was written, false if there was an error parsing the order.
        """
        try:
            pass
        except:
            pass

    def get(self, key: str) -> any:
        '''
        .. function:: get(key)

        Returns the value from the network cache corresponding to the provided ``key``

        .. note::
            Does not refresh the cache

        .. seealso::
            :mod: NetworkCache.refresh_cache()

        :param key: The key to pull out of the network cache
        :type key: str
        :returns: The deserialized value stored at the key in the cache
        '''
        return self._cache[key]

    def load_cache(self):
        '''
        ..
        :return:
        '''
        try:
            self._cache = SqliteDict(CACHE_FILENAME)
        except FileNotFoundError:
            pass
        except (OSError, IOError) as e:
            log_error('An error occurred trying to load the cache file: ' + str(e))

    def save_cache(self):
        try:
            self._cache.commit()
        except (OSError, IOError) as e:
            log_error('An error occurred trying to save the cache file: ' + str(e))


cache = NetworkService()