import sys
import tkinter as tk
from stage_four.ui.main_menu import MainMenu
from stage_four.ui.ship_creation import ShipCreationScreen
from stage_four.ui.battle_screen import BattleScreen
from stage_four.game.battle import Battle


class Game:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Морской бой')
        self.root.geometry('1000x700')
        self.root.configure(bg='#1a1a2e')

        self.current_screen = None
        self._show_main_menu()

        self.root.mainloop()

    def _show_main_menu(self):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = MainMenu(
            self.root,
            on_start_game=self._show_ship_creation
        )

    def _show_ship_creation(self):
        if self.current_screen:
            self.current_screen.destroy()

        self.current_screen = ShipCreationScreen(
            self.root,
            on_complete=self._start_battle
        )

    def _start_battle(self, ship_data):
        if self.current_screen:
            self.current_screen.destroy()

        battle = Battle(
            player_name=ship_data['name'],
            player_type=ship_data['type'],
            player_points=ship_data['points'],
            location=ship_data['location'],
            time_of_day=ship_data['time_of_day']
        )

        self.current_screen = BattleScreen(
            self.root,
            battle,
            on_battle_end=self._on_battle_end
        )

    def _on_battle_end(self, winner):
        print(f'Бой окончен. Победитель: {winner.name}')
        self.root.after(3000, self._show_main_menu)


if __name__ == '__main__':
    # Если запущено с флагом --console — консольный режим
    if '--console' in sys.argv:
        print('Морской бой (консольный режим)\n')
        battle = Battle()
        battle.fight()
    else:
        Game()