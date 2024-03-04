from cmath import pi

from asteroids.asteroid import *
from random import randint, random


class AsteroidGenerator:
    player_position = Position()

    def set_player_position(self, player_position):
        self.player_position = player_position

    def random_asteroid(self, direction: Position):
        center = direction
        r = randint(800, 999)
        angle = random()*pi*2
        x = cos(angle).real * r + center.x
        y = sin(angle).real * r + center.y
        radius = randint(30, 100)
        speed = randint(50, 100)
        angle = Position(x, y).get_angle_to_direction(direction) + (random()*2-1)*(pi/4)
        return Asteroid(x, y, angle, radius, speed)

    def add_asteroids(self, current_asteroid_list, number_to_add, player_position: Position):
        return current_asteroid_list + [self.random_asteroid(player_position) for _ in range(number_to_add)]