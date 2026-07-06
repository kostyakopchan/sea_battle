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
            player_skill = self.events.use_skill(self.player_ship, self.enemy_ship)

            # Проверка уклонения противника
            enemy_skill = self.events.use_skill(self.enemy_ship, self.player_ship)
            if self.events.check_dodge(enemy_skill, self.enemy_ship):
                self.events.log_dodge(self.player_ship, self.enemy_ship)
            else:
                # Применяем усиление урона игрока
                damage = self.events.apply_skill_effect(player_skill, self.player_ship, self.enemy_ship)

                # Применяем защиту противника
                actual_damage = self.events.apply_defense(enemy_skill, damage, self.enemy_ship)

                # Наносим урон
                self.enemy_ship.hp -= actual_damage
                self.events.log_attack(self.player_ship, self.enemy_ship, actual_damage)

            if not self.enemy_ship.is_alive():
                break

            # Ход противника
            enemy_skill = self.events.use_skill(self.enemy_ship, self.player_ship)

            # Проверка уклонения игрока
            player_skill = self.events.use_skill(self.player_ship, self.enemy_ship)
            if self.events.check_dodge(player_skill, self.player_ship):
                self.events.log_dodge(self.enemy_ship, self.player_ship)
            else:
                # Применяем усиление урона противника
                damage = self.events.apply_skill_effect(enemy_skill, self.enemy_ship, self.player_ship)

                # Применяем защиту игрока
                actual_damage = self.events.apply_defense(player_skill, damage, self.player_ship)

                # Наносим урон
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