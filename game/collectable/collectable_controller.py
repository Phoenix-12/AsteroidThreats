from collectable.collectable_view import *
from collectable.collectable_model import *


class CollectableController:
    def __init__(self, model: CollectableModel, view: CollectableView):
        self.view = view
        self.model = model

    def update(self, delta_time, player_position: Position):
        self.model.update(delta_time)
        #self.view.set_position(player_position, player_position.angle, self.model.collectables)
        #self.model.set_player_position(player_position)
