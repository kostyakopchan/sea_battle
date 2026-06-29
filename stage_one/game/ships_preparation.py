import random
from stage_one.entities import enemy, player
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

if __name__ == '__main__':
    battle_preparation = ShipsPreparation()
    print('___Игрок___')
    print(battle_preparation.get_player_ship())
    print('___')
    print('___Противник___')
    print(battle_preparation.get_enemy_ship())
    print('___')

