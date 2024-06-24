#!/usr/bin/env python3
'''
function that takes 2 int args and returns a tuple of size 2: a start indx
endindx corresponding to the range of indexes to return in a list for those
particular pagination parameters.
Page numbers are 1-indexed, i.e. the first page is page 1.
'''


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
