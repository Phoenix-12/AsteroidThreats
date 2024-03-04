
from player.Spaceship import *
from math import *

from utility.position import *


class AsteroidView:
    def __init__(self, height, root, canvas: tkinter.Canvas):
        self.HEIGHT = height
        self.root = root
        self.canvas = canvas
        # self.meteora_pict = tkinter.Image()
        #self.l = tkinter.Label(image=self.meteora_pict)
        #self.l.grid(row=0, column=0)
        self.view_asteroids = [canvas.create_oval(*[-1 for _ in range(4)], fill="red") for _ in range(50)]

    def set_position(self, player_position, player_angle, asteroids):
        i = 0
        for asteroid in asteroids:
            i += 1
            self.set_position_1(player_position, player_angle, asteroid.position, asteroid.radius,
                                self.view_asteroids[i])

    def set_position_1(self, player_position, player_angle, position, radius, view_asteroid):
        dist = position.get_distance(player_position)
        delta_x = (position.x - player_position.x)
        delta_y = (position.y - player_position.y)

        if delta_y > 0:
            position = Position(dist * cos(-pi/2 - player_angle + acos(delta_x / dist)),
                                dist * sin(-pi/2 - player_angle + acos(delta_x / dist)))
        elif delta_y <= 0:
            position = Position(dist * cos(-pi / 2 - player_angle - acos(delta_x / dist)),
                                dist * sin(-pi / 2 - player_angle - acos(delta_x / dist)))

        delta_view = self.HEIGHT / 2
        self.canvas.coords(view_asteroid, position.x - radius + delta_view, position.y - radius + delta_view,
                           position.x + radius + delta_view, position.y + radius + delta_view)
