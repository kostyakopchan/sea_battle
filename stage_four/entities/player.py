from .entity import Ship
from stage_four.entities.entities_config import SHIP_TYPES, POINTS_PER_STAT


class Player(Ship):
    def __init__(self):
        super().__init__()

    @classmethod
    def from_ui_data(cls, name, ship_type, points):
        """Создает корабль из данных UI"""
        instance = cls.__new__(cls)
        instance.name = name
        instance.type = ship_type
        instance.skill = SHIP_TYPES[ship_type]['skill']
        instance.points = points

        # Расчет ТТХ
        instance.hp = POINTS_PER_STAT['hp']['base'] + (points['hp'] * POINTS_PER_STAT['hp']['per_point'])
        instance.speed = POINTS_PER_STAT['speed']['base'] + (points['speed'] * POINTS_PER_STAT['speed']['per_point'])
        instance.damage = POINTS_PER_STAT['damage']['base'] + (
                    points['damage'] * POINTS_PER_STAT['damage']['per_point'])
        instance.armor = POINTS_PER_STAT['armor']['base'] + (points['armor'] * POINTS_PER_STAT['armor']['per_point'])

        instance.base_hp = instance.hp
        instance.base_speed = instance.speed
        instance.base_damage = instance.damage
        instance.base_armor = instance.armor

        return instance