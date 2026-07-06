from stage_one.entities.enemy import Enemy
from stage_one.entities.player import Player


class ShipsPreparation (Enemy, Player):
    def __init__(self):
        self.player_ship = self._set_player_ship()
        self.enemy_ship = self._set_enemy_ship()

    def _set_player_ship(self):
        return Player()

    def _set_enemy_ship(self):
        return Enemy()

    def get_player_ship(self):
        return self.player_ship.name

    def get_enemy_ship(self):
        return self.enemy_ship.name

    def get_ships(self):
        return self.player_ship, self.enemy_ship