#!/usr/bin/env python3
"""Module that implements a basic cache
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A class that represents a basic caching system that:
        - Adds an item to the cache
        - Fetches an item from the cache
    """

    def put(self, key, item):
        """Adds an item to cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Gets an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
