from utility.position import Position
import cmath


class Bullet:
    def __init__(self, pos: Position,radius=5, speed=500, add_speed=0):
        self.speed = speed + add_speed
        self.position = pos
        self.radius = radius

    def move(self, delta_time):
            self.position.x += delta_time*self.speed*cmath.cos(self.position.angle).real
            self.position.y += delta_time*self.speed*cmath.sin(self.position.angle).real