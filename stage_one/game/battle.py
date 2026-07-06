from .battle_events import Events
from .ships_preparation import ShipsPreparation


class Battle():
    def __init__(self):
        self.preparation = ShipsPreparation()
        self.player_ship, self.enemy_ship = self.preparation.get_ships()
        self.events = Events()

    def fight(self):
        print('\n___НАЧАЛО БИТВЫ___')
        print(f'{self.player_ship.name} VS {self.enemy_ship.name}\n')

        round_num = 1
        while self.player_ship.is_alive() and self.enemy_ship.is_alive():
            print(f'--- Раунд {round_num} ---')

            # Ход игрока
            self.events.use_skill(self.player_ship, self.enemy_ship)
            self.events.attack(self.player_ship, self.enemy_ship)

            if not self.enemy_ship.is_alive():
                break

            # Ход противника
            self.events.use_skill(self.enemy_ship, self.player_ship)
            self.events.attack(self.enemy_ship, self.player_ship)

            round_num += 1

        self.declare_winner()

    def declare_winner(self):
        print('\n___БИТВА ОКОНЧЕНА___')
        if self.player_ship.is_alive():
            print(f'ПОБЕДА: {self.player_ship.name}')
        else:
            print(f'ПОРАЖЕНИЕ: {self.enemy_ship.name} победил')

        print('\nЛог битвы:')
        for entry in self.events.get_log():
            print(f'  {entry}')