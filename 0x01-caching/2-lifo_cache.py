#!/usr/bin/env python3
'''
this class willm use the base class and the lifo technique.
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''this class will use data from the base class to perfom caching ops. '''
    def __init__(self):
        '''the init method'''
        super().__init__()
        self.order = []

    def put(self, key, item):
        '''must assign to the dict self.cache_data the item value of the ky'''
        if key is None or item is None:
            return

        if key not in self.cache_data:
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                removed_key = self.order.pop()
                del self.cache_data[removed_key]
                print("DISCARD: {}".format(removed_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        '''returns the value in self.cache_data linked to key'''
        if key is None:
            return None
        return self.cache_data.get(key)
