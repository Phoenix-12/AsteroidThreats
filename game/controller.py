import time

from utility.collision_system import *
from player.PlayerController import *
from utility.input_system import *
from asteroids.asteroid_controller import *
from model import *
from view import *
from player.bullets import Bullet
from utility import constants
from collectable.collectable_controller import CollectableController

class Controller:
    time_to_score = 0
    game_is_paused = False

    def __init__(self, model: Model, view: View):
        self.model = model
        self.view = view

        self.view.on_update(self.update)

        self.asteroid_controller = AsteroidController(self.model.asteroid_model, self.view.asteroid_view)
        self.player_controller = PlayerController(self.model.player_model, self.view.player_view)
        self.collectable_controller = CollectableController(self.model.collectable_model, self.view.collectable_view)

        self.view.on_motion(self.motion)
        self.input_system = InputSystem(self.key_press, self.key_release)
        self.collision_system = CollisionSystem()
        self.view.start_view(self.on_restart)

    def on_restart(self):
        self.model.restart()
        self.view.restart()

    def motion(self, event: tkinter.Event):
        self.player_controller.motion(event)

    def key_press(self, key: keyboard.Key):

        key = str(key)[1]
        if key == "x":
            self.player_controller.model.is_shooting = True

        if key == "w":
            self.player_controller.model.is_accelerating = True
        if key == "a":
            self.player_controller.model.turning_system.press_left()
        if key == "d":
            self.player_controller.model.turning_system.press_right()
        if key == "s":
            self.player_controller.model.turning_system.press_brake()

    def key_release(self, key):
        key = str(key)[1]
        if key == "r":
            self.model.restart()
        if key == "x":
            self.player_controller.model.is_shooting = False
        if key == "w":
            self.player_controller.model.is_accelerating = False
        if key == "a":
            self.player_controller.model.turning_system.release_left()
        if key == "d":
            self.player_controller.model.turning_system.release_right()
        if key == "s":
            self.player_controller.model.turning_system.release_brake()

    def update(self, delta_time):
        if self.collision_system.is_collision_player_with_asteroids(self.player_controller.get_radius(),
                                                                    self.player_controller.get_position(),
                                                                    self.asteroid_controller.model.asteroids):
            if self.model.player_model.is_alive:
                self.view.ui.death()
                self.game_is_paused = True
            self.model.player_model.is_alive = False

        ast: Asteroid
        bul: Bullet
        ast, bul = self.collision_system.is_collision_bullets_with_asteroids(self.player_controller.model.gun.bullets,
                                                                             self.asteroid_controller.model.asteroids)
        if ast and bul:
            for asteroid in self.asteroid_controller.model.asteroids:
                if bul.position.get_distance(asteroid.position) <= constants.bullet_explosion_radius + asteroid.radius:
                    asteroid.position.x = 100000000
                elif bul.position.get_distance(asteroid.position) <= constants.bullet_discarding_radius + asteroid.radius:
                    asteroid.position.angle = bul.position.get_angle_to_direction(asteroid.position)


            bul.position.x = -100000000
            #self.player_controller.model.gun.bullets.remove(bul)


        if self.game_is_paused and not self.model.player_model.is_alive:
            delta_time = 0

        if self.time_to_score > 1:
            self.time_to_score = 0
            self.model.player_model.score += 1
            self.view.ui.update_score(self.model.player_model.score)
        else:
            self.time_to_score += delta_time

        self.player_controller.update(delta_time)

        self.asteroid_controller.update(delta_time, self.player_controller.model.position,
                                        self.player_controller.model.position.angle)

        self.model.asteroid_model.spawn_asteroids()

        self.collectable_controller.update(delta_time, self.player_controller.model.position)

