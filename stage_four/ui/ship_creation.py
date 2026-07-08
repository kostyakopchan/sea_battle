import tkinter as tk
from tkinter import messagebox
from .widgets import StyledButton, StyledLabel, StyledEntry, StatSlider
from stage_four.entities.entities_config import SHIP_TYPES, LOCATIONS, TIME_OF_DAY, TOTAL_POINTS


class ShipCreationScreen:
    def __init__(self, root, on_complete):
        self.root = root
        self.on_complete = on_complete
        self.frame = tk.Frame(root, bg='#1a1a2e')
        self.frame.pack(fill='both', expand=True)

        self.remaining_points = TOTAL_POINTS
        self.sliders = {}

        self._create_widgets()

    def _create_widgets(self):
        # Заголовок
        title = StyledLabel(
            self.frame,
            text='Создание корабля',
            font=('Arial', 24, 'bold')
        )
        title.pack(pady=20)

        # Ввод имени
        name_frame = tk.Frame(self.frame, bg='#1a1a2e')
        name_frame.pack(pady=10)

        StyledLabel(name_frame, text='Имя корабля:').pack(side='left', padx=5)
        self.name_entry = StyledEntry(name_frame, width=30)
        self.name_entry.pack(side='left', padx=5)

        # Выбор типа
        type_frame = tk.Frame(self.frame, bg='#1a1a2e')
        type_frame.pack(pady=10)

        StyledLabel(type_frame, text='Тип корабля:').pack(side='left', padx=5)
        self.type_var = tk.StringVar(value=list(SHIP_TYPES.keys())[0])
        type_menu = tk.OptionMenu(
            type_frame,
            self.type_var,
            *list(SHIP_TYPES.keys())
        )
        type_menu.config(font=('Arial', 11), bg='white', width=25)
        type_menu.pack(side='left', padx=5)

        # Очки
        points_label = StyledLabel(
            self.frame,
            text=f'Всего очков: {TOTAL_POINTS}',
            font=('Arial', 14, 'bold')
        )
        points_label.pack(pady=10)
        self.points_label = points_label

        # Слайдеры для характеристик
        stats_frame = tk.Frame(self.frame, bg='#1a1a2e')
        stats_frame.pack(pady=20)

        for stat in ['hp', 'speed', 'damage', 'armor']:
            slider = StatSlider(stats_frame, stat, TOTAL_POINTS)
            slider.pack(pady=5)
            self.sliders[stat] = slider

        # Выбор локации
        location_frame = tk.Frame(self.frame, bg='#1a1a2e')
        location_frame.pack(pady=10)

        StyledLabel(location_frame, text='Локация:').pack(side='left', padx=5)
        self.location_var = tk.StringVar(value=list(LOCATIONS.keys())[0])
        location_menu = tk.OptionMenu(
            location_frame,
            self.location_var,
            *list(LOCATIONS.keys())
        )
        location_menu.config(font=('Arial', 11), bg='white', width=25)
        location_menu.pack(side='left', padx=5)

        # Выбор времени суток
        time_frame = tk.Frame(self.frame, bg='#1a1a2e')
        time_frame.pack(pady=10)

        StyledLabel(time_frame, text='Время суток:').pack(side='left', padx=5)
        self.time_var = tk.StringVar(value=list(TIME_OF_DAY.keys())[0])
        time_menu = tk.OptionMenu(
            time_frame,
            self.time_var,
            *list(TIME_OF_DAY.keys())
        )
        time_menu.config(font=('Arial', 11), bg='white', width=25)
        time_menu.pack(side='left', padx=5)

        # Кнопка подтверждения
        btn_confirm = StyledButton(
            self.frame,
            text='Начать бой',
            command=self._on_confirm,
            width=20,
            height=2
        )
        btn_confirm.pack(pady=20)

    def _on_confirm(self):
        # Проверка имени
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showerror('Ошибка', 'Введите имя корабля')
            return

        # Проверка очков
        total_used = sum(slider.get_value() for slider in self.sliders.values())
        if total_used != TOTAL_POINTS:
            messagebox.showerror(
                'Ошибка',
                f'Необходимо распределить ровно {TOTAL_POINTS} очков. '
                f'Сейчас использовано: {total_used}'
            )
            return

        # Собираем данные
        ship_data = {
            'name': name,
            'type': self.type_var.get(),
            'points': {stat: slider.get_value() for stat, slider in self.sliders.items()},
            'location': self.location_var.get(),
            'time_of_day': self.time_var.get()
        }

        self.frame.destroy()
        self.on_complete(ship_data)

    def destroy(self):
        self.frame.destroy()