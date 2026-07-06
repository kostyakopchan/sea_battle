class BattleEvents:
    def __init__(self, player_ship, enemy_ship):
        self.player = player_ship
        self.enemy = enemy_ship
        self.battle_log = []

    def attack(self, attacker, defender):
        """Атака одного корабля другим"""
        damage = attacker.attack(defender)
        log_entry = f'{attacker.name} атакует {defender.name} и наносит {damage} урона'
        self.battle_log.append(log_entry)
        print(log_entry)
        print(f'  → {defender.name}: HP {defender.hp}/{defender.max_hp}')

    @staticmethod
    def ability_active():
        """Заготовка для активации способностей"""
        from random import random
        return random() < 0.3  # 30% шанс активации

    def get_log(self):
        """Возвращает лог битвы"""
        return self.battle_log