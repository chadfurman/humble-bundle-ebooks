import os
import pickle
from utils.logger import log_error

CACHE_FILENAME = os.path.join(os.path.dirname(__file__), 'cache')
LIBRARY_PAGE_URL = 'https://humblebundle.com/home/library'
ORDER_ENDPOINT_URL = 'https://humblebundle.com/api/v1/order/%s'


class NetworkLayer(object):
    pass


# TODO: Convert NetworkCache to use SQLiteDict
class NetworkCache(object):
    _cache = None

    def __init__(self):
        self.load_cache()

    def refresh_cache(self):
        pass

    def get(self, key):
        pass

    def load_cache(self):
        try:
            with open(CACHE_FILENAME, 'rb') as cache_file:
                self._cache = pickle.loads(cache_file.read())
        except FileNotFoundError:
            pass
        except (OSError, IOError) as e:
            log_error('An error occurred trying to load the existing cache file: ' + str(e))

    def save_cache(self):
        try:
            with open(CACHE_FILENAME, 'wb') as cache_file:
                cache_file.write(pickle.dumps(self._cache))
        except (OSError, IOError) as e:
            log_error('An error occurred trying to save the cache file: ' + str(e))


cache = NetworkCache()