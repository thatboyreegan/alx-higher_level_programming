#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Represent a node in a singly-linked list."""
    def __init__(self, data, next_node=None):
        """Initialize a new Node.
        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """Get/set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if isinstance(value, Node) or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked lists."""
    def __init__(self):
        """Initialize a sngly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position
        in the list (increasing order).

        Args:
            value (int): Data for the new Node.
        """
        if self.head is None:
            self.head = Node(value)
        else:
            temp = self.head
            while temp is not None and temp.data < value:
                prev = temp
                temp = temp.next_node

            if temp == self.head:
                self.head = Node(value, self.head)
            elif temp is None:
                prev.next_node = Node(value)
            else:
                prev.next_node = Node(value, temp)

    def __str__(self):
        """Prints a string representation of this list."""

        temp = self.head
        while temp.next_node is not None:
            print(f"{temp.data}")
            temp = temp.next_node
        return str(temp.data)
