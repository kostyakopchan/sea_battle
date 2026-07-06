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

    def set_name(self):
        return input('Введите имя корабля: ')

    def set_type(self):
        return questionary.select('Выберите тип корабля:', choices=list(SHIP_TYPES.keys())).ask()

    def set_hp(self):
        return SHIP_TYPES[self.type]['hp']

    def set_speed(self):
        return SHIP_TYPES[self.type]['speed']

    def set_damage(self):
        return SHIP_TYPES[self.type]['damage']

    def set_armor(self):
        return SHIP_TYPES[self.type]['armor']

    def set_skill(self):
        return SHIP_TYPES[self.type]['skill']

    def attack(self, target):
        damage = max(1, self.damage - target.armor)
        target.hp -= damage
        return damage

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f'{self.name} ({self.type}) - HP: {self.hp}'