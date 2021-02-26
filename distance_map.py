"""Assignment 1 - Distance map (Task 1)

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

This module contains the class DistanceMap, which is used to store
and look up distances between cities. This class does not read distances
from the map file. (All reading from files is done in module experiment.)
Instead, it provides public methods that can be called to store and look up
distances.
"""
from typing import Dict, List, Tuple


class DistanceMap:
    """
    A distance that allows to look up the distance between any two cities
    == Instance Attributes ===
    None
    ==== Private Attributes =====
    _distance_track: Gives distance of two place. Each key is a starting point
    value is a list with destination and distance accordinngly
    """
    _distance_track: Dict[Tuple[str, str], int]

    def __init__(self):
        """
        Initialized with city A and City B to find the distance from A to B
        and vice Versa
        >>> d = DistanceMap()
        """
        self._distance_track = {}

    def distance(self, city_a: str, city_b: str) -> int:
        """
        Return distance from city1 to city2 is distance1,
        and the distance from city2 to city1 is distance2 or -1 if the distance
        is not stored in the _distance
        >>> m = DistanceMap()
        >>> m.add_distance('Montreal', 'Toronto', 4)
        >>> m.distance('Montreal', 'Toronto')
        4
        >>> s = DistanceMap()
        >>> s.distance('NYC','YYZ')
        -1
        """
        if (city_a, city_b) in self._distance_track:
            return self._distance_track[(city_a, city_b)]
        else:
            return -1

    def add_distance(self, city_a: str, city_b: str, dist1: int,
                     dist2: int = 1) -> None:
        """
        Adds a distance to the _distance_track.
        Need to be able to show distance from A to B and viceversa
        >>> m = DistanceMap()
        >>> m.distance('Montreal', 'Toronto') == -1
        True
        >>> m.add_distance('Montreal', 'Toronto', 4)
        >>> s = DistanceMap()
        >>> s.add_distance('NYC', 'YYZ',5, 10)
        >>> s.distance('YYZ', 'NYC')
        10
        """
        if (city_a, city_b) not in self._distance_track:
            self._distance_track[(city_a, city_b)] = dist1
            self._distance_track[(city_b, city_a)] = dist2


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': ['doctest', 'python_ta', 'typing'],
        'disable': ['E1136'],
        'max-attributes': 15,
    })
    import doctest

    doctest.testmod()
