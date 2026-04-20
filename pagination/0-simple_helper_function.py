#!/usr/bin/env python3
"""Module providing a helper function for pagination index calculation."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple of start and end indexes for a given page and page_size.

    Args:
        page: the page number (1-indexed)
        page_size: the number of items per page

    Returns:
        A tuple (start_index, end_index)
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
