SHIP_TYPES = {
    'Броненосец':{
        'hp': 1000,
        'speed': 5,
        'damage': 90,
        'armor': 100,
        'skill': 'Сопротивление урону'
        },
    'Торпедный катер':{
        'hp': 700,
        'speed': 4,
        'damage': 60,
        'armor': 70,
        'skill': 'Увеличенная скорость'
        },
    'Противокорабельная лодка':{
        'hp': 500,
        'speed': 10,
        'damage': 40,
        'armor': 50,
        'skill': 'Увеличенный урон'
        }
    }


# Система очков: сколько очков стоит каждая характеристика
POINTS_PER_STAT = {
    'hp': {'base': 100, 'per_point': 200},      # 1 очко = +200 HP
    'speed': {'base': 3, 'per_point': 2},       # 1 очко = +2 скорости
    'damage': {'base': 30, 'per_point': 15},    # 1 очко = +15 урона
    'armor': {'base': 20, 'per_point': 10},     # 1 очко = +10 брони
}

TOTAL_POINTS = 5  # Всего очков для распределения


LOCATIONS = {
    'Открытое море': {
        'description': 'Просторы океана, где манёвр решает всё',
        'events': [
            {'name': 'Внезапный шквал', 'effect': 'speed_down', 'value': 0.7, 'target': 'all', 'chance': 0.3},
            {'name': 'Попутный ветер', 'effect': 'speed_up', 'value': 1.3, 'target': 'all', 'chance': 0.3},
            {'name': 'Туман', 'effect': 'damage_down', 'value': 0.8, 'target': 'all', 'chance': 0.2},
        ]
    },
    'Архипелаг': {
        'description': 'Острова и узкие проливы',
        'events': [
            {'name': 'Мелководье', 'effect': 'speed_down', 'value': 0.5, 'target': 'all', 'chance': 0.3},
            {'name': 'Скрытая отмель', 'effect': 'damage_taken', 'value': 50, 'target': 'random', 'chance': 0.25},
            {'name': 'Узкий пролив', 'effect': 'armor_down', 'value': 0.8, 'target': 'all', 'chance': 0.2},
        ]
    },
    'Порт': {
        'description': 'Прибрежные воды с укреплениями',
        'events': [
            {'name': 'Береговая батарея', 'effect': 'damage', 'value': 40, 'target': 'random', 'chance': 0.25},
            {'name': 'Ремонтная команда', 'effect': 'heal', 'value': 80, 'target': 'random', 'chance': 0.25},
            {'name': 'Минное заграждение', 'effect': 'damage_taken', 'value': 70, 'target': 'random', 'chance': 0.2},
        ]
    }
}


TIME_OF_DAY = {
    'День': {'hp': 1.0, 'speed': 1.0, 'damage': 1.0, 'armor': 1.0},
    'Ночь': {'hp': 1.0, 'speed': 0.8, 'damage': 0.9, 'armor': 0.9},
    'Рассвет': {'hp': 1.0, 'speed': 1.1, 'damage': 1.0, 'armor': 1.0},
    'Закат': {'hp': 1.0, 'speed': 0.9, 'damage': 1.1, 'armor': 1.0},
    'Шторм': {'hp': 1.0, 'speed': 0.7, 'damage': 1.2, 'armor': 0.8},
}