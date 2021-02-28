"""
Question (6 marks)

Implement the function 'longest_sequence' according to the docstring provided.

You may use the Stack and Queue classes provided in module 'adts' to
create temporary Stack and/or Queue objects. These are the same Stack and
Queue classes you have seen before.

You must NOT create any other compound objects (lists, dictionaries, sets,
etc.)

You may create variables to store individual elements (counters, items that
have been popped or dequeued, etc.)

You may add doctest examples if desired.

Save your solution in a file called Q3_solution.py and hand it in on MarkUs.

--------------------------------------------------------------------------------
This code is provided solely for the personal and private use of students
taking the CSC148 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Diane Horton, Jonathan Calver, Sophia Huynh, Myriam Majedi,
and Jaisie Sin.
"""

from adts import Stack, Queue


def longest_sequence(q: Queue) -> int:
    """Return the length of the longest sequence in q with the same value.

    Queue q will contain the same elements in the same order before and after
    longest_sequence is called.

    Two items a and b are considered to have the same value if a == b.  If there
    are no items in q, the longest sequence has length 0.

    Preconditions:
    - the items in q can be compared using ==, !=, <, >, etc.

    >>> q = Queue()
    >>> q.enqueue(5)
    >>> q.enqueue(10)
    >>> q.enqueue(10)
    >>> q.enqueue(15)
    >>> longest_sequence(q)
    2
    >>> q.dequeue()
    5
    >>> q.dequeue()
    10
    >>> q.dequeue()
    10
    >>> q.dequeue()
    15
    >>> q.is_empty()
    True
    """
    # TODO: implement this function:
