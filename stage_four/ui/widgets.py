import tkinter as tk
from tkinter import ttk


class StyledButton(tk.Button):
    """Стилизованная кнопка"""

    def __init__(self, parent, text, command=None, **kwargs):
        # Устанавливаем дефолтные значения, если их нет в kwargs
        kwargs.setdefault('bg', '#4a90e2')
        kwargs.setdefault('fg', 'white')
        kwargs.setdefault('font', ('Arial', 12, 'bold'))
        kwargs.setdefault('relief', 'raised')
        kwargs.setdefault('bd', 3)
        kwargs.setdefault('cursor', 'hand2')

        self._default_bg = kwargs['bg']
        self._hover_bg = '#357abd'

        super().__init__(
            parent,
            text=text,
            command=command,
            **kwargs
        )

        self.bind('<Enter>', lambda e: self.config(bg=self._hover_bg))
        self.bind('<Leave>', lambda e: self.config(bg=self._default_bg))


class StyledLabel(tk.Label):
    """Стилизованный label"""

    def __init__(self, parent, text='', **kwargs):
        kwargs.setdefault('font', ('Arial', 11))
        kwargs.setdefault('bg', '#2c3e50')
        kwargs.setdefault('fg', 'white')

        super().__init__(
            parent,
            text=text,
            **kwargs
        )


class StyledEntry(tk.Entry):
    """Стилизованный entry"""

    def __init__(self, parent, **kwargs):
        kwargs.setdefault('font', ('Arial', 11))
        kwargs.setdefault('bg', 'white')
        kwargs.setdefault('fg', 'black')
        kwargs.setdefault('relief', 'solid')
        kwargs.setdefault('bd', 2)

        super().__init__(
            parent,
            **kwargs
        )


class StatSlider(tk.Frame):
    """Слайдер для распределения очков"""

    def __init__(self, parent, stat_name, max_value, current_value=0):
        super().__init__(parent, bg='#1a1a2e')
        self.stat_name = stat_name
        self.max_value = max_value
        self.value = tk.IntVar(value=current_value)

        self.label = StyledLabel(self, text=f'{stat_name}: ')
        self.label.pack(side='left', padx=5)

        self.scale = tk.Scale(
            self,
            from_=0,
            to=max_value,
            variable=self.value,
            orient='horizontal',
            length=200,
            bg='#2c3e50',
            fg='white',
            troughcolor='#0f3460',
            highlightthickness=0,
            command=self._update_label
        )
        self.scale.pack(side='left', padx=5)

        self.value_label = StyledLabel(self, text=str(current_value), width=3)
        self.value_label.pack(side='left', padx=5)

    def _update_label(self, val):
        self.value_label.config(text=str(int(val)))

    def get_value(self):
        return self.value.get()