from stage_one.entities.entities_config import SHIP_TYPES


class Ship:
    def __init__(self):
        self.name = self.set_name()
        self.type = self.set_type()
        self.hp = self.set_hp()
        self.max_hp = self.hp
        self.speed = self.set_speed()
        self.damage = self.set_damage()
        self.armor = self.set_armor()

    def set_name(self):
        return input('Введите имя корабля: ')

    def set_type(self):
        from questionary import select
        return select('Выберите тип корабля:', choices=list(SHIP_TYPES.keys())).ask()

    def set_hp(self):
        default = SHIP_TYPES[self.type]['hp']
        value = input(f'Введите HP (по умолчанию {default}): ')
        return int(value) if value else default

    def set_speed(self):
        default = SHIP_TYPES[self.type]['speed']
        value = input(f'Введите скорость (по умолчанию {default}): ')
        return int(value) if value else default

    def set_damage(self):
        default = SHIP_TYPES[self.type]['damage']
        value = input(f'Введите урон (по умолчанию {default}): ')
        return int(value) if value else default

    def set_armor(self):
        default = SHIP_TYPES[self.type].get('armor', 0)
        value = input(f'Введите броню (по умолчанию {default}): ')
        return int(value) if value else default

    def attack(self, target):
        """Атаковать цель"""
        raw_damage = max(1, self.damage - target.armor)
        target.hp -= raw_damage
        return raw_damage

    def use_ability(self, target=None):
        """
        Использование способности корабля.
        Возвращает модификатор урона или информацию о действии.
        """
        from random import random

        # 30% шанс активации способности
        if random() >= 0.3:
            return None

        if self.type == 'Броненосец':
            # Сопротивление урону: снижает входящий урон на 50% на один ход
            return {'type': 'defense', 'value': 0.5}

        elif self.type == 'Торпедный катер':
            # Увеличенная скорость: шанс уклониться от атаки
            return {'type': 'dodge', 'value': True}

        elif self.type == 'Противокорабельная лодка':
            # Увеличенный урон: следующая атака наносит x2 урона
            return {'type': 'damage_boost', 'value': 2.0}

        return None

    def is_alive(self):
        """Проверка жив ли корабль"""
        return self.hp > 0

    def __str__(self):
        return f'{self.name} ({self.type}) - HP: {self.hp}/{self.max_hp}'


class Player(Ship):
    pass


class Enemy(Ship):
    def set_name(self):
        return 'Вражеский корабль'

    def set_type(self):
        from random import choice
        return choice(list(SHIP_TYPES.keys()))

    def set_hp(self):
        return SHIP_TYPES[self.type]['hp']

    def set_speed(self):
        return SHIP_TYPES[self.type]['speed']

    def set_damage(self):
        return SHIP_TYPES[self.type]['damage']

    def set_armor(self):
        return SHIP_TYPES[self.type].get('armor', 0)