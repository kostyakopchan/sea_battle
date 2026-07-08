import tkinter as tk
from .widgets import StyledButton


class MainMenu:
    def __init__(self, root, on_start_game, on_network_game=None):
        self.root = root
        self.on_start_game = on_start_game
        self.on_network_game = on_network_game
        self.frame = tk.Frame(root, bg='#1a1a2e')
        self.frame.pack(fill='both', expand=True)

        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        title = tk.Label(
            self.frame,
            text='МОРСКОЙ БОЙ',
            font=('Arial', 32, 'bold'),
            bg='#1a1a2e',
            fg='#e94560'
        )
        title.pack(pady=50)

        # Подзаголовок
        subtitle = tk.Label(
            self.frame,
            text='Выберите режим игры',
            font=('Arial', 14),
            bg='#1a1a2e',
            fg='#a0a0a0'
        )
        subtitle.pack(pady=10)

        # Кнопка одиночной игры
        btn_single = StyledButton(
            self.frame,
            text='Одиночная игра',
            command=self.on_start_game,
            width=25,
            height=2
        )
        btn_single.pack(pady=10)

        # Кнопка сетевой игры (если передана функция)
        if self.on_network_game:
            btn_network = StyledButton(
                self.frame,
                text='Сетевая игра',
                command=self.on_network_game,
                width=25,
                height=2
            )
            btn_network.pack(pady=10)

        # Кнопка выхода
        btn_exit = StyledButton(
            self.frame,
            text='Выход',
            command=self.root.quit,
            width=25,
            height=2,
            bg='#e94560'
        )
        btn_exit.pack(pady=10)

    def destroy(self):
        self.frame.destroy()