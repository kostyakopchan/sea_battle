class BattleEvents:
    def __init__(self, player_ship, enemy_ship):
        self.player = player_ship
        self.enemy = enemy_ship
        self.battle_log = []
        self.player_ability_active = None
        self.enemy_ability_active = None

    def check_abilities(self):
        """Проверка активации способностей в начале раунда"""
        # Способность игрока
        player_ability = self.player.use_ability()
        if player_ability:
            self.player_ability_active = player_ability
            ability_text = self._get_ability_description(self.player, player_ability)
            log_entry = f'✨ {self.player.name} активирует способность: {ability_text}'
            self.battle_log.append(log_entry)
            print(log_entry)

        # Способность противника
        enemy_ability = self.enemy.use_ability()
        if enemy_ability:
            self.enemy_ability_active = enemy_ability
            ability_text = self._get_ability_description(self.enemy, enemy_ability)
            log_entry = f'✨ {self.enemy.name} активирует способность: {ability_text}'
            self.battle_log.append(log_entry)
            print(log_entry)

    def _get_ability_description(self, ship, ability):
        """Описание способности для лога"""
        if ability['type'] == 'defense':
            return 'Сопротивление урону (входящий урон -50%)'
        elif ability['type'] == 'dodge':
            return 'Уклонение (шанс избежать атаки)'
        elif ability['type'] == 'damage_boost':
            return 'Усиленная атака (урон x2)'
        return 'Неизвестная способность'

    def attack(self, attacker, defender):
        """Атака одного корабля другим с учётом способностей"""
        # Проверка уклонения (для Торпедного катера)
        defender_ability = (self.player_ability_active if defender == self.player
                            else self.enemy_ability_active)

        if defender_ability and defender_ability['type'] == 'dodge':
            from random import random
            if random() < 0.5:  # 50% шанс уклониться
                log_entry = (f'💨 {defender.name} уклоняется от атаки {attacker.name}!\n'
                             f'  → {defender.name}: HP {defender.hp}/{defender.max_hp}')
                self.battle_log.append(log_entry)
                print(log_entry)
                return 0

        # Расчёт урона
        base_damage = attacker.damage

        # Проверка усиления урона (для Противокорабельной лодки)
        attacker_ability = (self.player_ability_active if attacker == self.player
                            else self.enemy_ability_active)

        if attacker_ability and attacker_ability['type'] == 'damage_boost':
            base_damage = int(base_damage * attacker_ability['value'])

        # Расчёт урона с учётом брони
        raw_damage = max(1, base_damage - defender.armor)

        # Проверка сопротивления урону (для Броненосца)
        if defender_ability and defender_ability['type'] == 'defense':
            raw_damage = int(raw_damage * defender_ability['value'])
            raw_damage = max(1, raw_damage)  # минимум 1 урон

        # Применение урона
        defender.hp -= raw_damage

        # Логирование
        log_entry = (f'{attacker.name} атакует {defender.name}\n'
                     f'  Базовый урон: {base_damage} | Броня: {defender.armor} | '
                     f'Пробито: {raw_damage}\n'
                     f'  → {defender.name}: HP {defender.hp}/{defender.max_hp}')

        self.battle_log.append(log_entry)
        print(log_entry)

        # Сброс способностей после использования
        if attacker_ability:
            if attacker == self.player:
                self.player_ability_active = None
            else:
                self.enemy_ability_active = None

        if defender_ability:
            if defender == self.player:
                self.player_ability_active = None
            else:
                self.enemy_ability_active = None

        return raw_damage

    def get_log(self):
        """Возвращает лог битвы"""
        return self.battle_log