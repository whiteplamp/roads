from math import sqrt


class Point:
    def __init__(self, pos_x: int, pos_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y


class Road:
    def __init__(self, a: Point, b: Point):
        self.a = a,
        self.b = b
        self.size = sqrt((b.pos_x - a.pos_x) ** 2 + (b.pos_y - a.pos_y) ** 2)




