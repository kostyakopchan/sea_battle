import random


class Events():
    def __init__(self):
        self.log = []

    def attack(self, attacker, defender):
        damage = attacker.attack(defender)
        log_entry = f'{attacker.name} атакует {defender.name} и наносит {damage} урона'
        self.log.append(log_entry)
        print(log_entry)
        print(f'У {defender.name} осталось {defender.hp} HP')

    @staticmethod
    def ability_active():
        return random.choice([True, False])

    def use_skill(self, ship, target):
        if not self.ability_active():
            return

        if ship.skill == 'Сопротивление урону':
            print(f'{ship.name} использует Сопротивление урону!')
            ship.armor *= 2
        elif ship.skill == 'Увеличенная скорость':
            print(f'{ship.name} использует Увеличенную скорость и уклоняется!')
            return 'dodge'
        elif ship.skill == 'Увеличенный урон':
            print(f'{ship.name} использует Увеличенный урон!')
            ship.damage *= 2

    def get_log(self):
        return self.log