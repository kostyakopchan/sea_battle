import questionary
from stage_four.entities.enemy import Enemy
from stage_four.entities.player import Player
from stage_four.entities.entities_config import LOCATIONS, TIME_OF_DAY


class ShipsPreparation(Enemy, Player):
    def __init__(self):
        self.player_ship = self._set_player_ship()
        self.enemy_ship = self._set_enemy_ship()
        self.location = self._set_location()
        self.time_of_day = self._set_time_of_day()

    def _set_player_ship(self):
        return Player()

    def _set_enemy_ship(self):
        return Enemy()

    def _set_location(self):
        return questionary.select(
            'Выберите боевую локацию:',
            choices=list(LOCATIONS.keys())
        ).ask()

    def _set_time_of_day(self):
        return questionary.select(
            'Выберите время суток:',
            choices=list(TIME_OF_DAY.keys())
        ).ask()

    def get_player_ship(self):
        return self.player_ship.name

    def get_enemy_ship(self):
        return self.enemy_ship.name

    def get_ships(self):
        return self.player_ship, self.enemy_ship

    def get_location(self):
        return self.location

    def get_time_of_day(self):
        return self.time_of_day

    def show_ships_info(self):
        """Выводит информацию о кораблях"""
        print('\n___Игрок___')
        print(f'Имя: {self.player_ship.name}')
        print(f'Тип: {self.player_ship.type}')
        print(f'ТТХ: HP={self.player_ship.hp}, Скорость={self.player_ship.speed}, '
              f'Урон={self.player_ship.damage}, Броня={self.player_ship.armor}')
        print(f'Очки: {self.player_ship.points}')
        print('___')

        print('\n___Противник___')
        print(f'Имя: {self.enemy_ship.name}')
        print(f'Тип: {self.enemy_ship.type}')
        print(f'ТТХ: HP={self.enemy_ship.hp}, Скорость={self.enemy_ship.speed}, '
              f'Урон={self.enemy_ship.damage}, Броня={self.enemy_ship.armor}')
        print(f'Очки: {self.enemy_ship.points}')
        print('___')

        print(f'\n___Локация: {self.location}___')
        print(f'___Время суток: {self.time_of_day}___')


if __name__ == '__main__':
    battle_preparation = ShipsPreparation()
    battle_preparation.show_ships_info()