import questionary
from .entities_config import SHIP_TYPES, POINTS_PER_STAT, TOTAL_POINTS


class Ship:

    def __init__(self):
        self.name = self.set_name()
        self.type = self.set_type()
        self.skill = self.set_skill()

        # Распределение очков
        self.points = self.distribute_points()

        # Расчет ТТХ на основе очков
        self.hp = self.calculate_hp()
        self.speed = self.calculate_speed()
        self.damage = self.calculate_damage()
        self.armor = self.calculate_armor()

        # Базовые значения для модификаторов
        self.base_hp = self.hp
        self.base_speed = self.speed
        self.base_damage = self.damage
        self.base_armor = self.armor

    def set_name(self):
        return input('Введите имя корабля: ')

    def set_type(self):
        return questionary.select('Выберите тип корабля:', choices=list(SHIP_TYPES.keys())).ask()

    def set_skill(self):
        return SHIP_TYPES[self.type]['skill']

    def distribute_points(self):
        """Распределяет очки по характеристикам"""
        print(f'\nУ вас {TOTAL_POINTS} очков для распределения.')
        print('Доступные характеристики: hp, speed, damage, armor\n')

        points = {'hp': 0, 'speed': 0, 'damage': 0, 'armor': 0}
        remaining = TOTAL_POINTS

        while remaining > 0:
            print(f'Осталось очков: {remaining}')
            stat = questionary.select(
                'Выберите характеристику:',
                choices=['hp', 'speed', 'damage', 'armor']
            ).ask()

            max_for_stat = remaining
            amount = int(input(f'Сколько очков в {stat} (макс {max_for_stat}): '))

            if amount > max_for_stat:
                print(f'Можно вложить максимум {max_for_stat} очков')
                continue

            points[stat] += amount
            remaining -= amount

        return points

    def calculate_hp(self):
        base = POINTS_PER_STAT['hp']['base']
        per_point = POINTS_PER_STAT['hp']['per_point']
        return base + (self.points['hp'] * per_point)

    def calculate_speed(self):
        base = POINTS_PER_STAT['speed']['base']
        per_point = POINTS_PER_STAT['speed']['per_point']
        return base + (self.points['speed'] * per_point)

    def calculate_damage(self):
        base = POINTS_PER_STAT['damage']['base']
        per_point = POINTS_PER_STAT['damage']['per_point']
        return base + (self.points['damage'] * per_point)

    def calculate_armor(self):
        base = POINTS_PER_STAT['armor']['base']
        per_point = POINTS_PER_STAT['armor']['per_point']
        return base + (self.points['armor'] * per_point)

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