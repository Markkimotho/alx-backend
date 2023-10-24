#!/usr/bin/env python3
"""Simple helper function module
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Return the start and end index for the given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
