from stage_one.game.battle_events import BattleEvents


class Battle:
    def __init__(self, player_ship, enemy_ship):
        self.player = player_ship
        self.enemy = enemy_ship
        self.events = BattleEvents(player_ship, enemy_ship)

    def fight(self):
        """Основной цикл боя"""
        print('\n' + '=' * 60)
        print('НАЧАЛО БИТВЫ')
        print('=' * 60)
        print(f'{self.player.name} VS {self.enemy.name}\n')

        round_num = 1
        while self.player.is_alive() and self.enemy.is_alive():
            print(f'\n--- Раунд {round_num} ---')

            # Ход игрока
            self.events.attack(self.player, self.enemy)

            if not self.enemy.is_alive():
                break

            # Ход противника
            self.events.attack(self.enemy, self.player)

            round_num += 1

        self._declare_winner()

    def _declare_winner(self):
        """Объявление победителя"""
        print('\n' + '=' * 60)
        print('БИТВА ОКОНЧЕНА')
        print('=' * 60)

        if self.player.is_alive():
            print(f'🏆 ПОБЕДА: {self.player.name}')
            print(f'   Осталось HP: {self.player.hp}/{self.player.max_hp}')
        else:
            print(f'💀 ПОРАЖЕНИЕ: {self.enemy.name} победил')
            print(f'   У него осталось HP: {self.enemy.hp}/{self.enemy.max_hp}')

        print('\nЛог битвы:')
        for entry in self.events.get_log():
            print(f'  • {entry}')