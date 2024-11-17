from math import sqrt
from typing import List


class Point:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.pos_x == other.pos_x and self.pos_y == other.pos_y
        return False

    def __str__(self):
        return f"x: {self.pos_x} y: {self.pos_y}"


class Road:
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b
        self.size = sqrt((b.pos_x - a.pos_x) ** 2 + (b.pos_y - a.pos_y) ** 2)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.a == other.a and self.b == other.b
        return False

    def __str__(self):
        return f"{self.a} ---{self.size}--- {self.b}"


class RoadMap:
    def __init__(self, roads: List[Road]):
        self.roads = roads

    def __str__(self):
        _str = ""
        for road in self.roads:
            _str += f"{str(road)}\n"
        return _str
