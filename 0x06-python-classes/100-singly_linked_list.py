#!/usr/bin/python3
"""
Module 100-singly_linked_list
Defines class Node
Defines class SinglyLinkedList
"""


class Node:
    """
    class Square definition

    Args:
        data:
        next_node:

    Functions:
        __init__
        data(self)
        data(self, value)
        next_node(self)
        next_node(self, value)
    """

    def __init__(self, data, next_node=None):
        """
        initialixes node

        Attributes:
            data:
            next_node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter

        Return: data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter

        Args:
            value:
        """
        if not (isinstance(value, (int))):
            raise TypeError(f"data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter

        Return:next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter

        Args:
            value:
        """
        if type(value) is not Node and value is not None:
            raise TypeError(f"next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    class SinglyLinkedList

    Args:
        head:

    Functions:
    __initII(self)
    sorted_insert(self, value)
    """

    def __init__(self):
        """
        Inititalize

        Attributes:
            head:
        """
        self.__head = None

    def __str__(self):
        """
        String representation
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp.data)
            tmp = tmp.next_node
            if tmp is not None:
                string += "\n"
        return string

    def sorted_insert(self, value):
        """
        inserts new node in a sorted order

        Args:
            value:
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return

        tmp = self.__head
        if new.data < tmp.data:
            new.next_node = self.__head
            self.__head = new
            return

        while (tmp.next_node is not None) and (new.data > tmp.next_node.data):
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new
        return
