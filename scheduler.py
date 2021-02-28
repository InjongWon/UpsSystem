"""Assignment 1 - Scheduling algorithms (Task 4)

CSC148, Winter 2021

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Authors: Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Myriam Majedi, and Jaisie Sin.

All of the files in this directory and all subdirectories are:
Copyright (c) 2021 Diane Horton, Ian Berlott-Atwell, Jonathan Calver,
Sophia Huynh, Myriam Majedi, and Jaisie Sin.

===== Module Description =====

This module contains the abstract Scheduler class, as well as the two
subclasses RandomScheduler and GreedyScheduler, which implement the two
scheduling algorithms described in the handout.
"""
from typing import List, Dict, Union, Callable
from random import random, shuffle, choice
from container import PriorityQueue
from domain import Parcel, Truck


class Scheduler:
    """A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.

    This is an abstract class.  Only child classes should be instantiated.
    """

    def schedule(self, parcels: List[Parcel], trucks: List[Truck],
                 verbose: bool = False) -> List[Parcel]:
        """Schedule the given <parcels> onto the given <trucks>, that is, decide
        which parcels will go on which trucks, as well as the route each truck
        will take.

        Mutate the Truck objects in <trucks> so that they store information
        about which parcel objects they will deliver and what route they will
        take.  Do *not* mutate the list <parcels>, or any of the parcel objects
        in that list.

        Return a list containing the parcels that did not get scheduled onto any
        truck, due to lack of capacity.

        If <verbose> is True, print step-by-step details regarding
        the scheduling algorithm as it runs.  This is *only* for debugging
        purposes for your benefit, so the content and format of this
        information is your choice; we will not test your code with <verbose>
        set to True.
        """
        raise NotImplementedError


class RandomScheduler:
    """
    A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.
    ===== Private Attributes =====
    _schedule:
    A list that contains all the parcels that did not get scheduled
    """
    _schedule: List[Parcel]

    def __init__(self) -> None:
        """

        Initialize
        ===== Private Attributes =====
        _schedule:
        A list that contains all the parcels that did not get scheduled
        """
        self._schedule = []

    def schedule(self, parcels: List[Parcel], trucks: List[Truck],
                 verbose: bool = False) -> List[Parcel]:
        """Schedule the given <parcels> onto the given <trucks>, that is, decide
        which parcels will go on which trucks, as well as the route each truck
        will take.

        The random algorithm will go through the parcels in random order.
        For each parcel, it will schedule it onto a randomly chosen truck
        (from among those trucks that have capacity to add that parcel).
        Because of this randomness, each time you run your random algorithm
        on a given problem, it may generate a different solution.
        """
        lst = parcels.copy()
        have_capacity = []
        random_parcel = random.choice(parcels)
        for truck in trucks:
            if truck.fullness() < random_parcel.volume:
                have_capacity.append(truck)
        random_truck = random.choice(have_capacity)
        if random_truck.fullness() < float(random_parcel.volume * 10):
            random_truck.pack(random_parcel)
            lst.remove(random_parcel)
        return lst


class GreedyScheduler:
    """
    A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.
    ===== Private Attributes =====
    _info:
    A Dictionary that contains all information about parcel and truck
        {depot_location:the name of the city where each parcels is,
        and from which it must be delivered to its destination.
        Also the city where all trucks start at and return to,
        parcel_file: the name of a file containing parcel data,
        truck_file: the name of a file containing truck data,
        map_file: the name of a file containing distance data,algorithm: either
        ‘random’ or ‘greedy’. If ‘random’, none of the remaining keys
        are required in the configuration file (and if they are present,
        they will be ignored),
        parcel_priority: either ‘volume’ or ‘destination’.,
        parcel_order: either
        ‘non-decreasing’ (meaning we process parcels in order from smallest
        to largest), or ‘non-increasing’ (meaning we process parcels in order
        from largest to smallest).,
        truck_order: either
        ‘non-decreasing’ (meaning we choose the eligible truck
        with the least available space, and as go through the parcels we will
        choose trucks with greater available space), or
        ‘non-increasing’ (meaning we choose the eligible truck with the most
        available space, and as we go through the parcels we will choose trucks
        with less available space),
        verbose: either true or false. Note the lack of quote marks;
        the code we’ve written to read in the configuration dictionary
        can read such values directly into a boolean.
    """
    _info: Dict[str, str]

    def __init__(self, configure: Dict[str, str]) -> None:
        self.configure = configure

    def schedule(self, parcels: List[Parcel], trucks: List[Truck],
                 verbose: bool = False) -> List[Parcel]:
        """

        Schedule the given <parcels> onto the given <trucks>, that is, decide
        which parcels will go on which trucks, as well as the route each truck
        will take.
        it tries to pick the “best” truck it can for each parcel.
        Our greedy algorithm is quite short-sighted: it makes each choice
        without looking ahead to possible consequences of the choice
        (that’s why we call it “greedy”).

        """
        pass
# TODO: Implement classes RandomScheduler and GreedyScheduler.


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'allowed-io': ['compare_algorithms'],
        'allowed-import-modules': ['doctest', 'python_ta', 'typing',
                                   'random', 'container', 'domain'],
        'disable': ['E1136'],
        'max-attributes': 15,
    })
