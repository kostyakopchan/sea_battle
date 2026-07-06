import random
from stage_two.entities.entities_config import LOCATIONS


class Events():
    def __init__(self, location):
        self.log = []
        self.location = location

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

    def random_event(self, player_ship, enemy_ship):
        """Проверяет и применяет случайное событие локации"""
        events_pool = LOCATIONS[self.location]['events']

        # 30% шанс, что событие произойдёт в этом раунде
        if not random.choice([True, False]) and random.random() > 0.3:
            return

        # Выбираем случайное событие из пула
        event = random.choice(events_pool)

        # Проверяем шанс конкретного события
        if random.random() > event['chance']:
            return

        # Применяем эффект события
        self._apply_event_effect(event, player_ship, enemy_ship)

    def _apply_event_effect(self, event, player_ship, enemy_ship):
        """Применяет эффект события к кораблям"""
        event_name = event['name']
        effect = event['effect']
        value = event['value']
        target = event['target']

        log_entry = f'⚡ Событие: {event_name}'
        self.log.append(log_entry)
        print(log_entry)

        # Определяем цели
        if target == 'all':
            targets = [player_ship, enemy_ship]
        elif target == 'random':
            targets = [random.choice([player_ship, enemy_ship])]
        else:
            targets = []

        for ship in targets:
            if effect == 'speed_down':
                ship.speed = max(1, int(ship.speed * value))
                print(f'  → {ship.name}: скорость снижена до {ship.speed}')
            elif effect == 'speed_up':
                ship.speed = int(ship.speed * value)
                print(f'  → {ship.name}: скорость увеличена до {ship.speed}')
            elif effect == 'damage_down':
                ship.damage = max(1, int(ship.damage * value))
                print(f'  → {ship.name}: урон снижен до {ship.damage}')
            elif effect == 'damage':
                ship.hp = max(0, ship.hp - value)
                print(f'  → {ship.name} получает {value} урона (осталось {ship.hp} HP)')
            elif effect == 'damage_taken':
                ship.hp = max(0, ship.hp - value)
                print(f'  → {ship.name} получает {value} урона (осталось {ship.hp} HP)')
            elif effect == 'heal':
                ship.hp = min(ship.base_hp, ship.hp + value)
                print(f'  → {ship.name} восстанавливает {value} HP (теперь {ship.hp} HP)')
            elif effect == 'armor_down':
                ship.armor = max(0, int(ship.armor * value))
                print(f'  → {ship.name}: броня снижена до {ship.armor}')

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