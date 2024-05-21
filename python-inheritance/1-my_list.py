#!/usr/bin/python3
"""
A class MyList that inherits from list
"""


class MyList(list):
    """
    class MyList inherited from list
    """

    def print_sorted(self):
        sorted_list = sorted(self)
        """
        prints the list (ascending sort)
        """
        print(sorted_list)
