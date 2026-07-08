import random
from stage_three.entities.entities_config import SHIP_TYPES, POINTS_PER_STAT, TOTAL_POINTS


class Enemy():
    def __init__(self):
        self.type = self.set_type()
        self.name = f'Вражеский(ая) {self.type}'
        self.skill = self.set_skill()

        # Автоматическое распределение очков
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

    def set_type(self):
        return random.choice(list(SHIP_TYPES.keys()))

    def set_skill(self):
        return SHIP_TYPES[self.type]['skill']

    def distribute_points(self):
        """Автоматически распределяет очки"""
        points = {'hp': 0, 'speed': 0, 'damage': 0, 'armor': 0}
        remaining = TOTAL_POINTS

        # Случайное распределение
        while remaining > 0:
            stat = random.choice(['hp', 'speed', 'damage', 'armor'])
            points[stat] += 1
            remaining -= 1

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
        return f'{self.name} - HP: {self.hp}'