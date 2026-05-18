import questionary
from .ships_config import SHIP_TYPES


class Ship:
    def __init__(self):
        self.name = input('Введите имя корабля: ')
        self.type = self.set_type()
        self.hp = self.set_hp()
        self.speed = self.set_speed()
        self.damage = self.set_damage()
        self.skill = self.set_skill()

    def set_type(self):
        return questionary.select('Выберите тип корабля: ', choices=(list(SHIP_TYPES.keys()))).ask()

    def set_hp(self):
        return SHIP_TYPES[self.type]['hp']

    def set_speed(self):
        return SHIP_TYPES[self.type]['speed']

    def set_damage(self):
        return SHIP_TYPES[self.type]['damage']

    def set_skill(self):
        return SHIP_TYPES[self.type]['skill']
