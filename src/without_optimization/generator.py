from random import randrange
from typing import List

from src.without_optimization.structures import RoadMap, Point, Road


class Generator:
    MAX_SIZE_MAP = 10_000

    def __init__(self, points: int, roads: int, map_size_x: int, map_size_y: int):
        """
             roads: int -> roads <= n(n-1)/2, where n - points
             map_size_x <= MAX_SIZE_MAP (By default = 10 000)
        """
        if roads > points * (points - 1) / 2:
            raise ValueError("Points cant be less zero")

        if map_size_x > self.MAX_SIZE_MAP or map_size_y > self.MAX_SIZE_MAP:
            raise ValueError("You have been reached max map size")

        self.points = points
        self.roads = roads
        self.map_size_x = map_size_x
        self.map_size_y = map_size_y

    @classmethod
    def get_random_int_between(cls, start: int, stop: int, step: int = 20) -> int:
        """Choose a random item from range(start, stop[, step])"""
        if step != 1:
            return randrange(start=start, stop=stop, step=step)
        return randrange(start=start, stop=stop)

    @classmethod
    def get_random_point_from_list(cls, points: List[Point], exclude: Point = None) -> Point:
        """exclude needed to select other points"""
        n = cls.get_random_int_between(0, len(points))
        buf_n = n
        if points[n] == exclude:
            while buf_n == n:
                buf_n = cls.get_random_int_between(0, len(points))

        return points[buf_n]

    def generate_map_with_all_roads(self) -> RoadMap:
        points = list()
        roads = []

        for _ in range(self.points):
            pos_x = self.get_random_int_between(0, self.map_size_x)
            pos_y = self.get_random_int_between(0, self.map_size_y)
            points.append(Point(pos_x, pos_y))

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                roads.append(Road(a=points[i], b=points[j]))

        return RoadMap(roads=roads)

    def generate_map(self) -> RoadMap:
        points = list()
        roads = []

        for _ in range(self.points):
            pos_x = self.get_random_int_between(0, self.map_size_x)
            pos_y = self.get_random_int_between(0, self.map_size_y)
            points.append(Point(pos_x, pos_y))

        for _ in range(self.roads):
            point_a = self.get_random_point_from_list(points)
            point_b = self.get_random_point_from_list(points, exclude=point_a)

            road = Road(a=point_a, b=point_b)
            while road in roads:
                point_a = self.get_random_point_from_list(points)
                point_b = self.get_random_point_from_list(points, exclude=point_a)
                road = Road(a=point_a, b=point_b)

            roads.append(
                road
            )

        return RoadMap(roads=roads)
