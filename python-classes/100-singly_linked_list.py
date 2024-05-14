#!/usr/bin/python3

'''A class node that defines a ndoe of a singly linked list'''
class Node:
    ''' constructor'''
    def __init__(self, data, next_node=None):
        ''' private instance attribute data and next_node'''
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        ''' getter'''
        return self._data

    @data.setter
    def data(self, value):
        ''' setter'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value

''' A class that defines a singly linked list '''
class SinglyLinkedList:
    ''' constructor '''
    def __init__(self):
        ''' private instance attribute head'''
        self.head = None

    def __str__(self):
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result

    def sorted_insert(self, value):
        ''' public instance method'''
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
            return

        current = self.head
        while current.next_node is not None and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node
