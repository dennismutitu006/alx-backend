#!/usr/bin/env python3
'''
this is a class that is set to inherit components from the base class
'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    ''' BasicCache defines:
    - a caching syst without a limit
    '''
    def put(self, key, item):
        '''
        assings to the dict self.cache_data the itme value for the key key.
        '''
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in the self.cache_data linked to the key.
        '''
        if key is None:
            return None

        return self.cache_data.get(key)
