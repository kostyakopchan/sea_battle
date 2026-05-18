import random
from stage_one.game.ships_preparation import BattlePreparation


class Battle:
    def __init__(self):
        self.ships = BattlePreparation()

    def attack(self):
        pass

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