from math import *
from utility.position import *
from player.TurningSystem import *
import player.bullets
from player.gun import Gun

class PlayerModel:
    turn_speed = 1.66*pi

    def __init__(self, x=0, y=0, angle=3*pi / 2, base_acceleration=1000, speed=0, radius=20):
        self.score = 0
        self.position = Position(x, y, angle)
        self.base_acceleration = base_acceleration
        self.speed = speed
        self.radius = radius
        self.is_alive = True
        self.time = 0
        self.is_accelerating = False
        self.turning_system = TurningSystem()
        self.is_shooting = False
        self.oxygen: float = 15
        self.gun = Gun()

    def turn(self, delta_time):
        self.position.angle += self.turn_speed * self.turning_system.get_direction() * delta_time

    def slowdown(self, delta_time):
        if self.turning_system.is_braking:
            self.speed -= self.base_acceleration * 2 * delta_time
            if self.speed < 4:
                self.speed = 0

    def is_able_to_shoot(self):
        return self.gun.is_able_to_shoot()

    def shoot(self):
        shoot_pos = Position(self.position.x, self.position.y, self.position.angle)
        self.gun.shoot(shoot_pos, self.speed)

    def move(self, delta_time):
        moving = self.speed * delta_time
        self.position.x += moving * cos(self.position.angle)
        self.position.y += moving * sin(self.position.angle)

        self.gun.update(delta_time)

    def accelarate(self, delta_time):
        if self.is_accelerating:
            self.speed += delta_time * self.base_acceleration

    def stop(self):
        self.speed = 0

    def is_alive(self):
        return self.is_alive

    def restart(self):
        self.__init__()
