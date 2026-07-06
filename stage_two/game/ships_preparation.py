import questionary
from stage_two.entities.enemy import Enemy
from stage_two.entities.player import Player
from stage_two.entities.entities_config import LOCATIONS, TIME_OF_DAY


class ShipsPreparation (Enemy, Player):
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