from .battle_events import Events
from .ships_preparation import ShipsPreparation
from stage_four.entities.entities_config import TIME_OF_DAY, LOCATIONS
from stage_four.entities.player import Player
from stage_four.entities.enemy import Enemy


class Battle():
    def __init__(self, player_name=None, player_type=None, player_points=None,
                 location=None, time_of_day=None):

        # Если данные переданы из UI — используем их
        if player_name and player_type and player_points:
            self.player_ship = Player.from_ui_data(player_name, player_type, player_points)
            self.enemy_ship = Enemy()
            self.location = location
            self.time_of_day = time_of_day
        else:
            # Старая логика для консольного режима
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

    def execute_round(self):
        """Выполняет один раунд боя (для UI режима)"""
        # Случайное событие
        self.events.random_event(self.player_ship, self.enemy_ship)

        # Проверка смерти после события
        if not self.player_ship.is_alive() or not self.enemy_ship.is_alive():
            return

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
            return

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

    def fight(self):
        """Консольный бой (для обратной совместимости)"""
        print('\n___НАЧАЛО БИТВЫ___')
        print(f'{self.player_ship.name} VS {self.enemy_ship.name}\n')

        round_num = 1
        while self.player_ship.is_alive() and self.enemy_ship.is_alive():
            print(f'--- Раунд {round_num} ---')
            self.execute_round()
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