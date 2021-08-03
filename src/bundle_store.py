from network_cache import NetworkCache

# TODO: use NetworkCache and let NetworkCache use SqliteDict
class BundleStore(object):
    def __init__(self, cache: NetworkCache) -> None:
        self.cache = cache

    def get_all_bundle_ids(self):
        return []