import questionary
from .entities_config import SHIP_TYPES


class Ship:

    def __init__(self):
        self.name = self.set_name()
        self.type = self.set_type()
        self.hp = self.set_hp()
        self.speed = self.set_speed()
        self.damage = self.set_damage()
        self.armor = self.set_armor()
        self.skill = self.set_skill()

        # Базовые значения для модификаторов
        self.base_hp = self.hp
        self.base_speed = self.speed
        self.base_damage = self.damage
        self.base_armor = self.armor

    def set_name(self):
        return input('Введите имя корабля: ')

    def set_type(self):
        return questionary.select('Выберите тип корабля:', choices=list(SHIP_TYPES.keys())).ask()

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
        default = SHIP_TYPES[self.type]['armor']
        value = input(f'Введите броню (по умолчанию {default}): ')
        return int(value) if value else default

    def set_skill(self):
        return SHIP_TYPES[self.type]['skill']

    def apply_time_modifiers(self, time_modifiers):
        """Применяет модификаторы времени суток к ТТХ"""
        self.hp = int(self.base_hp * time_modifiers['hp'])
        self.speed = int(self.base_speed * time_modifiers['speed'])
        self.damage = int(self.base_damage * time_modifiers['damage'])
        self.armor = int(self.base_armor * time_modifiers['armor'])

    def attack(self, target):
        damage = max(1, self.damage - target.armor)
        target.hp -= damage
        return damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f'{self.name} ({self.type}) - HP: {self.hp}'