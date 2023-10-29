#!/usr/bin/env python3
"""Module that implements the LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A class that implements a LIFO cache replacement policy
    """

    def __init__(self):
        """Initialize : Inherits from BaseCaching
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                newest_key = self.queue.pop()
                del self.cache_data[newest_key]
                print(f"DISCARD: {newest_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Gets an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
