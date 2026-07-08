import tkinter as tk
from .widgets import StyledButton, StyledLabel


class BattleScreen:
    def __init__(self, root, battle, on_battle_end):
        self.root = root
        self.battle = battle
        self.on_battle_end = on_battle_end
        self.frame = tk.Frame(root, bg='#1a1a2e')
        self.frame.pack(fill='both', expand=True)

        self._create_widgets()
        self._update_display()

    def _create_widgets(self):
        # Заголовок
        self.title_label = tk.Label(
            self.frame,
            text='БИТВА',
            font=('Arial', 24, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        self.title_label.pack(pady=10)

        # Информация о кораблях
        ships_frame = tk.Frame(self.frame, bg='#1a1a2e')
        ships_frame.pack(pady=20)

        # Игрок
        player_frame = tk.Frame(ships_frame, bg='#2c3e50', relief='raised', bd=2)
        player_frame.pack(side='left', padx=20)

        self.player_name_label = tk.Label(
            player_frame,
            text=self.battle.player_ship.name,
            font=('Arial', 16, 'bold'),
            bg='#2c3e50',
            fg='#4ecca3'
        )
        self.player_name_label.pack(pady=5, padx=20)

        self.player_hp_label = tk.Label(
            player_frame,
            text=f'HP: {self.battle.player_ship.hp}/{self.battle.player_ship.base_hp}',
            font=('Arial', 12),
            bg='#2c3e50',
            fg='white'
        )
        self.player_hp_label.pack(pady=5, padx=20)

        self.player_stats_label = tk.Label(
            player_frame,
            text=f'Урон: {self.battle.player_ship.damage} | Броня: {self.battle.player_ship.armor}',
            font=('Arial', 11),
            bg='#2c3e50',
            fg='#a0a0a0'
        )
        self.player_stats_label.pack(pady=5, padx=20)

        # VS
        vs_label = tk.Label(
            ships_frame,
            text='VS',
            font=('Arial', 20, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        vs_label.pack(side='left', padx=20)

        # Противник
        enemy_frame = tk.Frame(ships_frame, bg='#2c3e50', relief='raised', bd=2)
        enemy_frame.pack(side='left', padx=20)

        self.enemy_name_label = tk.Label(
            enemy_frame,
            text=self.battle.enemy_ship.name,
            font=('Arial', 16, 'bold'),
            bg='#2c3e50',
            fg='#e94560'
        )
        self.enemy_name_label.pack(pady=5, padx=20)

        self.enemy_hp_label = tk.Label(
            enemy_frame,
            text=f'HP: {self.battle.enemy_ship.hp}/{self.battle.enemy_ship.base_hp}',
            font=('Arial', 12),
            bg='#2c3e50',
            fg='white'
        )
        self.enemy_hp_label.pack(pady=5, padx=20)

        self.enemy_stats_label = tk.Label(
            enemy_frame,
            text=f'Урон: {self.battle.enemy_ship.damage} | Броня: {self.battle.enemy_ship.armor}',
            font=('Arial', 11),
            bg='#2c3e50',
            fg='#a0a0a0'
        )
        self.enemy_stats_label.pack(pady=5, padx=20)

        # Лог боя
        log_frame = tk.Frame(self.frame, bg='#1a1a2e')
        log_frame.pack(pady=10, fill='both', expand=True)

        log_title = tk.Label(
            log_frame,
            text='Лог боя:',
            font=('Arial', 12, 'bold'),
            bg='#1a1a2e',
            fg='white'
        )
        log_title.pack(anchor='w', padx=10)

        self.log_text = tk.Text(
            log_frame,
            height=15,
            width=80,
            bg='#0f3460',
            fg='white',
            font=('Courier', 10),
            relief='solid',
            bd=2,
            insertbackground='white'
        )
        self.log_text.pack(pady=5, padx=10, fill='both', expand=True)

        # Кнопка следующего хода
        self.btn_next = StyledButton(
            self.frame,
            text='Следующий ход',
            command=self._next_turn,
            width=20,
            height=2
        )
        self.btn_next.pack(pady=10)

    def _update_display(self):
        """Обновляет отображение HP и статов"""
        self.player_hp_label.config(
            text=f'HP: {self.battle.player_ship.hp}/{self.battle.player_ship.base_hp}'
        )
        self.enemy_hp_label.config(
            text=f'HP: {self.battle.enemy_ship.hp}/{self.battle.enemy_ship.base_hp}'
        )

        self.player_stats_label.config(
            text=f'Урон: {self.battle.player_ship.damage} | Броня: {self.battle.player_ship.armor}'
        )
        self.enemy_stats_label.config(
            text=f'Урон: {self.battle.enemy_ship.damage} | Броня: {self.battle.enemy_ship.armor}'
        )

        # Обновляем лог
        self.log_text.delete('1.0', tk.END)
        for entry in self.battle.events.get_log():
            self.log_text.insert(tk.END, entry + '\n')
        self.log_text.see(tk.END)

    def _next_turn(self):
        """Выполняет следующий ход"""
        # Проверяем условие победы
        if not self.battle.player_ship.is_alive() or not self.battle.enemy_ship.is_alive():
            self._end_battle()
            return

        # Выполняем один раунд
        self.battle.execute_round()
        self._update_display()

        # Проверяем условие победы после раунда
        if not self.battle.player_ship.is_alive() or not self.battle.enemy_ship.is_alive():
            self._end_battle()

    def _end_battle(self):
        """Завершает бой"""
        self.btn_next.config(state='disabled')

        # Определяем, кто победил
        if self.battle.player_ship.is_alive():
            # Победил игрок
            self.title_label.config(text=f'ПОБЕДА! {self.battle.player_ship.name} выиграл!', fg='#4ecca3')
        else:
            # Победил противник
            self.title_label.config(text=f'ПОРАЖЕНИЕ! {self.battle.enemy_ship.name} выиграл!', fg='#e94560')

        self.on_battle_end(self.battle.player_ship if self.battle.player_ship.is_alive() else self.battle.enemy_ship)

    def destroy(self):
        self.frame.destroy()