#!/usr/bin/env python3
"""Module that implements the MRU caching policy
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class that implements the MRU cache replacement policy
    """
    def __init__(self):
        """Initialize: Inherit from BaseCaching
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                mru_key = self.queue.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Gets an item from the cache
        """
        if key is not None and key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
