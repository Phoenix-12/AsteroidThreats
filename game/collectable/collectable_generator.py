import abc
from cmath import pi

from collectable.collectable import *
from random import randint, random


class CollectableGenerator:
    player_position = Position()

    def set_player_position(self, player_position):
        self.player_position = player_position

    def random_collectable(self, direction: Position):
        center = direction
        r = randint(800, 999)
        angle = random()*pi*2
        x = cos(angle).real * r + center.x
        y = sin(angle).real * r + center.y
        radius = randint(30, 100)
        speed = randint(50, 100)
        angle = Position(x, y).get_angle_to_direction(direction) + (random()*2-1)*(pi/4)
        return Collectable(x, y, angle, radius, speed)

    def add_items(self, current_collectable_list, number_to_add, player_position: Position):
        return current_collectable_list + [self.random_collectable(player_position) for _ in range(number_to_add)]
