#!/usr/bin/env python3
"""
A class named CountedIterator that wraps around an iterator
and keeps count of the number of items retrieved.
"""


class CountedIterator:
    """
    A class named CountedIterator
    """

    def __init__(self, iterable):
        """
        Initialize the CountedIterator with an iterable and a counter.
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Return the current value of the counter.
        """
        return self.counter

    def __iter__(self):
        """
        Return the iterator itself.
        """
        return self

    def __next__(self):
        """
        Fetch the next item, increment the counter
        and raise StopIteration when at the end.
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
