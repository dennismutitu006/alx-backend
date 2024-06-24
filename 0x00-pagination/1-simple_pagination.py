#!/usr/bin/env python3
'''
function that takes 2 int args and returns a tuple of size 2: a start indx
endindx corresponding to the range of indexes to return in a list for those
particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
'''
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''the get page function'''
        assert type(page_size) is int and type(page) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        i = index_range(page, page_size)
        if i[0] >= len(self.__dataset):
            return []
        else:
            return self.__dataset[i[0]:i[1]]
def index_range(page: int, page_size: int) -> tuple:
    '''
    Parameters:
        page: the page number.
        page_size: the number of characters for one page.

    Returns:
        a tuple with start index and end index.
    '''

    start_ind = (page - 1) * page_size
    end_ind = start_ind + page_size

    return (start_ind, end_ind)
