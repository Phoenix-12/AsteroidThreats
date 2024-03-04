from utility import constants
from utility.position import Position
from asteroids.asteroid_generator import *
from collectable.collectable_generator import *

class CollectableModel:
    def __init__(self):
        self.collectable_generator = CollectableGenerator()
        self.player_position = Position()
        self.collectables = self.collectable_generator.add_items([], constants.number_of_items, self.player_position)

    def update(self, delta_time):
        for collectable in self.collectables:
            collectable.move(delta_time)
            if collectable.position.get_distance(self.player_position) >= constants.distance_of_item_destroying:
                self.collectables = self.collectable_generator.add_items(self.collectables, 1, self.player_position)
                self.collectables.remove(collectable)

    def spawn_collectables(self, how_many=5):
        if len(self.collectables) < how_many:
            self.collectable_generator.add_items(self.collectables, how_many - len(self.collectables), self.player_position)

    def restart(self):
        self.player_position = Position(0, 0)
        self.collectables = self.collectable_generator.add_items([], self.number_of_asteroids, self.player_position)
