#!/usr/bin/env python3
"""
Extending Python List with Notifications
"""


class VerboseList(list):

    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, amount):
        super().extend(amount)
        print(f"Extended the list with [{len(amount)}] items.")

    def remove(self, item):
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=None):
        if index is not None:
            print(f"Popped [{self[index]}] from the list.")
            return super().pop(index)
        else:
            print(f"Popped [{self[-1]}] from the list.")
            return super().pop()


v_list = VerboseList([])

"""
Tests
v_list.append(4)
v_list.extend([2, 3])
v_list.remove(2)
v_list.pop()
"""
