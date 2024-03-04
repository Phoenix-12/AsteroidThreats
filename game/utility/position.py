import math
from math import floor, pi

class Position():
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f"x:{floor(self.x)} y:{floor(self.y)}"

    def get_distance(self, another_position):
        return ((self.x - another_position.x) ** 2 + (self.y - another_position.y) ** 2) ** 0.5

    def get_angle_to_direction(self, another_position):
        dist = self.get_distance(another_position)
        delta_x = (self.x - another_position.x)
        delta_y = (self.y - another_position.y)
        if delta_x == 0:
            if delta_y > 0:
                return pi/2
            if delta_y <= 0:
                return -pi/2
        elif delta_x > 0:
            return math.atan(delta_y/delta_x) + pi
        else:
            return math.atan(delta_y/delta_x)

    def get_delta_angle(self):
        pass
