import random
from .ships_preparation import ShipsPreparation


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
            return None

        if ship.skill == 'Сопротивление урону':
            print(f'{ship.name} использует {ship.skill}!')
            return {'type': 'defense', 'multiplier': 1.4}

        elif ship.skill == 'Увеличенная скорость':
            print(f'{ship.name} использует {ship.skill}!')
            return {'type': 'dodge', 'multiplier': 1.4}

        elif ship.skill == 'Увеличенный урон':
            print(f'{ship.name} использует {ship.skill}!')
            return {'type': 'damage_boost', 'multiplier': 1.4}

        return None

    def apply_skill_effect(self, skill_effect, attacker, defender):
        """Применяет эффект способности к атаке"""
        if not skill_effect:
            return attacker.damage

        damage = attacker.damage

        if skill_effect['type'] == 'damage_boost':
            damage = int(damage * skill_effect['multiplier'])
            log_entry = f'  → Урон увеличен на 40%: {damage}'
            self.log.append(log_entry)
            print(log_entry)

        return damage

    def check_dodge(self, skill_effect, defender):
        """Проверяет уклонение с учётом скорости"""
        if skill_effect and skill_effect['type'] == 'dodge':
            dodge_chance = min(0.8, defender.speed / 20)
            if random.random() < dodge_chance:
                log_entry = f'  → {defender.name} уклоняется благодаря скорости!'
                self.log.append(log_entry)
                print(log_entry)
                return True
        return False

    def apply_defense(self, skill_effect, damage, defender):
        """Применяет сопротивление урону"""
        if skill_effect and skill_effect['type'] == 'defense':
            reduced_damage = int(damage / skill_effect['multiplier'])
            log_entry = f'  → {defender.name} снижает урон на 40%: {reduced_damage}'
            self.log.append(log_entry)
            print(log_entry)
            return max(1, reduced_damage)
        return damage

    def log_attack(self, attacker, defender, damage):
        """Логирует атаку"""
        log_entry = f'{attacker.name} атакует {defender.name} и наносит {damage} урона'
        self.log.append(log_entry)
        print(log_entry)
        log_entry = f'У {defender.name} осталось {defender.hp} HP'
        self.log.append(log_entry)
        print(log_entry)

    def log_dodge(self, attacker, defender):
        """Логирует уклонение"""
        log_entry = f'{attacker.name} промахивается!'
        self.log.append(log_entry)
        print(log_entry)

    def get_log(self):
        return self.log