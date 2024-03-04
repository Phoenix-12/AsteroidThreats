from player.PlayerModel import PlayerModel
from asteroids.asteroid_model import *
from collectable.collectable_model import *

class Model:
    def __init__(self):
        self.player_model = PlayerModel()
        self.asteroid_model = AsteroidModel()
        self.collectable_model = CollectableModel()

    def check_collision(self, object_1, object_2):
        if object_1.radius + object_2.radius <= object_1.position.get_distance(object_2.position):
            print(f"{object_1}, {object_2} столкнулись!!")

    def restart(self):

        self.player_model.restart()
        self.asteroid_model.restart()
