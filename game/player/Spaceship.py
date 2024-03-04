import math

from utility.position import *
from math import *
import tkinter


class Spaceship:
    def __init__(self, canvas: tkinter.Canvas):
        self.angle = 0
        self.newpos = Position()
        self.canvas = canvas
        self.height = self.canvas.winfo_reqheight()
        self.cannon = canvas.create_polygon(0, 0, 100, 100, 200, 50, 70, 30, fill="white")
        self.spaceship = self.canvas.create_oval(0, 0, 100, 100, fill="white")

    def set_angle(self, newpos):
        self.newpos = newpos

    def set_spaceship(self,position, radius, angle):
        def set_space_cannon(self):
            x = self.height / 2
            y = self.height / 2

            angle = -pi/2

            pos = [cos(angle + pi / 20) * radius*3, sin(angle + pi / 20) * radius*3,
                   cos(angle - pi / 20) * radius*3, sin(angle - pi / 20) * radius*3,
                   cos(angle - 3 / 4 * pi) * radius, sin(angle - 3 / 4 * pi) * radius,
                   cos(angle + 3 / 4 * pi) * radius, sin(angle + 3 / 4 * pi) * radius]
            arr = []
            for i in pos:
                arr.append(i + self.height / 2)
            self.canvas.coords(self.cannon, *arr)

        set_space_cannon(self)
        self.canvas.coords(self.spaceship, self.height / 2 - radius,
                           self.height / 2 - radius,
                           self.height / 2 + radius,
                           self.height / 2 + radius)
