from .battle_events import Events
from .ships_preparation import ShipsPreparation
from stage_two.entities.entities_config import TIME_OF_DAY, LOCATIONS


class Battle():
    def __init__(self):
        self.preparation = ShipsPreparation()
        self.player_ship, self.enemy_ship = self.preparation.get_ships()
        self.location = self.preparation.get_location()
        self.time_of_day = self.preparation.get_time_of_day()
        self.events = Events(self.location)

        # Применяем модификаторы времени суток
        self._apply_time_modifiers()

    def _apply_time_modifiers(self):
        """Применяет модификаторы времени суток к ТТХ кораблей"""
        time_modifiers = TIME_OF_DAY[self.time_of_day]
        self.player_ship.apply_time_modifiers(time_modifiers)
        self.enemy_ship.apply_time_modifiers(time_modifiers)

        print(f'\n___Условия боя___')
        print(f'Локация: {self.location} — {LOCATIONS[self.location]["description"]}')
        print(f'Время суток: {self.time_of_day}')
        print(f'___')

    def fight(self):
        print('\n___НАЧАЛО БИТВЫ___')
        print(f'{self.player_ship.name} VS {self.enemy_ship.name}\n')

        round_num = 1
        while self.player_ship.is_alive() and self.enemy_ship.is_alive():
            print(f'--- Раунд {round_num} ---')

            # Случайное событие локации
            self.events.random_event(self.player_ship, self.enemy_ship)

            # Проверка смерти после события
            if not self.player_ship.is_alive() or not self.enemy_ship.is_alive():
                break

            # Ход игрока
            player_skill = self.events.use_skill(self.player_ship, self.enemy_ship)
            enemy_skill = self.events.use_skill(self.enemy_ship, self.player_ship)

            if self.events.check_dodge(enemy_skill, self.enemy_ship):
                self.events.log_dodge(self.player_ship, self.enemy_ship)
            else:
                damage = self.events.apply_skill_effect(player_skill, self.player_ship, self.enemy_ship)
                actual_damage = self.events.apply_defense(enemy_skill, damage, self.enemy_ship)
                self.enemy_ship.hp -= actual_damage
                self.events.log_attack(self.player_ship, self.enemy_ship, actual_damage)

            if not self.enemy_ship.is_alive():
                break

            # Ход противника
            enemy_skill = self.events.use_skill(self.enemy_ship, self.player_ship)
            player_skill = self.events.use_skill(self.player_ship, self.enemy_ship)

            if self.events.check_dodge(player_skill, self.player_ship):
                self.events.log_dodge(self.enemy_ship, self.player_ship)
            else:
                damage = self.events.apply_skill_effect(enemy_skill, self.enemy_ship, self.player_ship)
                actual_damage = self.events.apply_defense(player_skill, damage, self.player_ship)
                self.player_ship.hp -= actual_damage
                self.events.log_attack(self.enemy_ship, self.player_ship, actual_damage)

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