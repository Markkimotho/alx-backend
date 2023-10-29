#!/usr/bin/env python3
"""Module that implements a FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """A class that implements a FIFO cache replacement policy
    """
    def __init__(self):
        """Initialize : Inherit from BaseCaching
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Adds an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.queue:
                    oldest_key = self.queue.pop(0)
                    del self.cache_data[oldest_key]
                    print(f"DISCARD: {oldest_key}")
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Gets an item from the cache
        """
        if key is not None:
            return self.cache_data.get(key)
        return None
