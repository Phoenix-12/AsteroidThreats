import tkinter
from player.PlayerView import *
from asteroids.asteroid_view import *
from user_interface import *
from collectable.collectable_view import *

class View:
    def __init__(self):
        self.HEIGHT = 1000
        self.root = tkinter.Tk()
        self.root.geometry(f"{self.HEIGHT}x{self.HEIGHT}+0+0")
        self.canvas = tkinter.Canvas(height=self.HEIGHT, width=self.HEIGHT, background="#11003b")


        self.bg = tkinter.PhotoImage(file="sprites/stars_1.png")
        self.canvas.create_image(500, 500, image=self.bg)

        self.canvas.grid(row=0, column=0)


        self.root.update()
        self.asteroid_view = AsteroidView(self.HEIGHT, self.root, self.canvas)
        self.player_view = PlayerView(self.HEIGHT, self.root, self.canvas)
        self.collectable_view = CollectableView
        self.ui = UI(self.HEIGHT, self.root, self.canvas)

    def on_motion(self, motion):
        self.root.bind("<Motion>", motion)

    def start_view(self, on_restart):
        self.ui.on_restart = on_restart
        self.player_view.start_view()
        self.game_loop()

    def game_loop(self):
        delta_time = 0
        while True:
            s_t = time()
            self.update_controller(delta_time)
            self.root.update()
            e_t = time()
            delta_time = e_t - s_t

    def on_motion(self, func):
        self.root.bind("<Motion>", func)

    def on_update(self, function):
        self.update_controller = function

    def restart(self):
        self.ui.restart()
