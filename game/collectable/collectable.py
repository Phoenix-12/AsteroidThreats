from cmath import cos, sin
from utility.position import Position


class Collectable():
    def __init__(self, x, y, angle, radius, type="None", speed=0):
        self.position = Position(x, y, angle)
        self.radius = radius
        self.speed = speed
        self.picked_up = False
        self.type: str = type

    def move(self, delta_time):
        angle = self.position.angle

        self.position = Position(self.position.x + (cos(angle)*self.speed*delta_time).real,
                                 self.position.y + (sin(angle)*self.speed*delta_time).real,
                                 angle)

