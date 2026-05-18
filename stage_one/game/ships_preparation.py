import random
from stage_one.ships.ships import Ship
from stage_one.ships.ships_config import SHIP_TYPES


class BattlePreparation:
    def __init__(self):
        self.player_ship = self._set_player_ship()
        self.player_ship_name = self._set_player_ship_name()
        self.player_ship_type = self._set_player_ship_type()
        self.player_ship_params = self._set_player_ship_params()
        self.enemy_ship = self._set_enemy_ship()
        self.enemy_ship_params = self._set_enemy_ship_params()

    def _set_player_ship(self):
        return Ship()

    def _set_player_ship_name(self):
        return self.player_ship.name

    def _set_player_ship_type(self):
        return self.player_ship.type

    def _set_player_ship_params(self):
        return SHIP_TYPES[self.player_ship.type]

    def _set_enemy_ship(self):
        return random.choice(list(SHIP_TYPES))

    def _set_enemy_ship_params(self):
        return SHIP_TYPES[self.enemy_ship]

    def get_player_ship(self):
        return self.player_ship

    def get_player_ship_name(self):
        return self.player_ship_name

    def get_player_ship_type(self):
        return self.player_ship_type

    def get_player_ship_params(self):
        return self.player_ship_params

    def get_enemy_ship(self):
        return self.enemy_ship

    def get_enemy_ship_params(self):
        return self.enemy_ship_params

if __name__ == '__main__':
    battle_preparation = BattlePreparation()
    print('___')
    print(battle_preparation.get_player_ship_name())
    print('___')
    print(battle_preparation.get_player_ship_type())
    print('___')
    print(battle_preparation.get_player_ship_params())
    print('___')
    print(battle_preparation.get_enemy_ship())
    print('___')
    print(battle_preparation.get_enemy_ship_params())
    print('___')

