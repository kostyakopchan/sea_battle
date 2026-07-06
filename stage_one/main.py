from stage_one.game.ships_preparation import ShipsPreparation
from stage_one.game.battle import Battle

if __name__ == '__main__':
    print('Морской бой - Модуль 1\n')

    # Подготовка кораблей
    print('=== Подготовка кораблей ===\n')
    print('Игрок 1:')
    preparation = ShipsPreparation()
    player_ship, enemy_ship = preparation.get_ships()

    print(f'\nКорабль игрока: {player_ship}')
    print(f'Корабль противника: {enemy_ship}\n')

    # Начало боя
    input('Нажмите Enter для начала боя...')

    battle = Battle(player_ship, enemy_ship)
    battle.fight()