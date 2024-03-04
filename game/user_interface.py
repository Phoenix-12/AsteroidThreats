import tkinter
from time import *
from tkinter import ttk

from utility.position import Position

class UI:
    on_restart = None

    def __init__(self, height, root, canvas: tkinter.Canvas):
        self.HEIGHT = height
        self.root: tkinter.Tk = root
        self.canvas = canvas

        #self.main_menu = tkinter.Menu()
        #self.root.configure(menu=self.main_menu)

        self.score = ttk.Label(text="Score: 0", font=("Arial", 40))
        self.score.grid(row=0, column=0, sticky='n')

        self.root.bind('<r>', self.f)

    def update_score(self, score):
        self.score.configure(text="Score: " + str(score))

    def f(self, event):
        self.restart()

    def death(self):
        self.death_text = ttk.Label(text="YOU ARE DEAD...", foreground="red", background="black", font=("Arial", 80))
        self.restart_button = ttk.Button(text="RESTART", command=self.on_restart)

        self.death_text.grid(row=0, column=0)
        self.restart_button.grid(row=0, column=0, sticky="s", pady=300)

    def restart(self):
        self.update_score(0)
        self.restart_button.destroy()
        self.death_text.destroy()

    def start_view(self):
        pass
