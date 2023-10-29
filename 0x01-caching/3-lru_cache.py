#!/usr/bin/env python3
"""Module that implements the LRU caching policy
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """A class that implements the LRU cache replacement policy
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
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                lru_key = self.queue.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")
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
