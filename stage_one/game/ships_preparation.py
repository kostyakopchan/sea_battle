from stage_one.entities.entity import Player, Enemy


class ShipsPreparation:
    def __init__(self):
        self.player_ship = Player()
        self.enemy_ship = Enemy()

    def get_ships(self):
        """Возвращает корабли игрока и противника"""
        return self.player_ship, self.enemy_ship