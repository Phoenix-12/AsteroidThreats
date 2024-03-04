from player.PlayerModel import *
from player.PlayerView import *


class PlayerController:
    def __init__(self, model: PlayerModel, view: PlayerView):
        self.model = model
        self.view = view

    def update(self, delta_time):
        self.model.slowdown(delta_time)
        self.model.move(delta_time)
        self.view.move(self.model.position, self.model.radius, self.model.position.angle)
        self.model.accelarate(delta_time)
        self.model.turn(delta_time)
        self.view.show_bullets(self.model.position, self.model.position.angle, self.model.gun.bullets)
        if self.model.is_shooting:
            self.model.shoot()

    def motion(self, event: tkinter.Event):
        return
        self.view.spaceship.set_angle(Position(event.x, event.y))

    def brake(self):
        self.model.slowdown()

    def accelerate(self, delta_time):
        self.model.accelarate(delta_time)

    def get_radius(self):
        return self.model.radius

    def get_position(self):
        return self.model.position
