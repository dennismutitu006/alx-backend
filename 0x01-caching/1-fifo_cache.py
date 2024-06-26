#!/usr/bin/env python3
'''
A class that inherits from BaseCaching and is a caching system
following the FIFO technique.
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    The FIFO method of cache replacement.
    '''
    def __init__(self):
        '''Initialize'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''Assign to the dict self.cache_data the item value of the key.'''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''Return the value of the dict linked to the key'''
        if key is None:
            return None
        return self.cache_data.get(key)
