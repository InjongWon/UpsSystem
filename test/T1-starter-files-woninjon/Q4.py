"""
Question (10 marks)

Below is a new linked list method called repeat_greater_than_first. It has at
least one bug in its implementation. We have provided the parts of the
LinkedList class that you need for this question. Do NOT add to it or modify it,
other than as instructed below.

There are two parts to this question:

(a) Write a pytest function called test_demo_pass that the buggy implementation
    passes and another called test_demo_fail that the buggy implementation
    fails.

    Both tests must pass on a working implementation of the function (a version
    without any bugs).

    Both must be different from the doctest example provided, and must be
    meaningful test cases that check the method's behaviour relative to its
    docstring specification.

    Write these functions at the bottom of this file (under the TODO).

(b) Find and fix the bug(s) in the method repeat_greater_than_first.

Save your solution in a file called Q4_solution.py and submit it on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from __future__ import annotations
from typing import Any, Optional
import pytest


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class LinkedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    _first: Optional[_Node]

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        if len(items) == 0:  # No items, and an empty list!
            self._first = None
        else:
            self._first = _Node(items[0])
            curr = self._first
            for item in items[1:]:
                curr.next = _Node(item)
                curr = curr.next

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(LinkedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(LinkedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def repeat_greater_than_first(self) -> None:
        """Duplicate every node in this LinkedList that is greater than the
        first node.

        Specifically, for every original node in this LinkedList containing a
        value greater than the value in the first node, duplicate the node by
        inserting a new node after it that has the same value.

        An original node is a node that was part of this LinkedList before
        any insertions by this method.

        Preconditions:
        - This LinkedList is not empty.
        - This LinkedList contains only integers.

        >>> lst = LinkedList([2, 1, 4, 1])
        >>> lst.repeat_greater_than_first()
        >>> str(lst)
        '[2 -> 1 -> 4 -> 4 -> 1]'
        """
        # TODO: Find and fix the bug(s) in this method.
        first = None
        curr = self._first
        if curr is not None:
            first = curr.item
        while curr.next is not None:
            if curr.item > first:
                new_node = _Node(curr.item)
                new_node.next = curr.next
                curr.next = new_node
                curr = new_node.next
            else:
                curr = curr.next


# TODO: Write the two required pytest functions below.
#       - test_demo_pass should pass the buggy implementation provided and pass
#         on a working implementation.
#       - test_demo_fail should fail the buggy implementation provided but pass
#         on a working implementation.


if __name__ == '__main__':
    pytest.main(['Q4_solution.py'])
