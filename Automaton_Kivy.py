'''
TODO:
1. Go to main menu:
    1.1 Display main menu title DONE
    1.2 Display automaton size label + entry box DONE
    1.3 Display wraparound label + checkbutton DONE
    1.4 Display start button with label of Start on top of it DONE
    1.5 Display Special Configurations button to go to Special Configurations screen
    1.6 Start button should be disabled as long as automaton size is not inputted
2. Automaton game:
    2.1 Display title.
    2.2 Display board with initial state.
    2.3 Display play button to start the automaton.
    2.4 Display Iterate Once button to iterate the board once.
    2.5 Display the Pause button to pause iterations.
    2.6 Display the Main Menu button to return to main menu.
3. Special Configuration:
    3.1 Display title.
    3.2 List special configurations, sectionated by type (gliders, traffic light etc.)
    3.3 List items should be buttons that leads to Automaton game, loaded with
        a specific initial state (the setting of the initial state is handled by
        LogicManager)
'''
from http.cookiejar import cut_port_re

from kivy.config import Config
from pygments.lexers import j

# Set the initial window position BEFORE importing any UI modules
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', '100')   # X coordinate from the left of the screen
Config.set('graphics', 'top', '50')    # Y coordinate from the top of the screen

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.graphics import Color
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

from LogicManager import LogicManager

FONT_PATH = "Fonts/Montserrat-Medium.ttf"

class Cell(Widget):

    color = ListProperty([0, 0, 0, 1])

    def __init__(self, pos: (int, int), size: (int, int), color: (int, int, int, int)):
        super().__init__()

        self.pos = pos
        self.size = size
        self.color = color

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

class GameScreen(Screen):
    def __init__(self, dimension: int, logic: LogicManager, **kwargs):
        super().__init__(**kwargs)

        self.grid: [[Cell]] = []
        self.grid_size = dimension
        self.logic = logic
        self.playing = False

        self.main_layout = BoxLayout(orientation="horizontal", spacing=dp(50))

        # Game Controls
        self.controls = BoxLayout(
            orientation="vertical",
            size_hint=(None, 1),
            size=(dp(200), dp(100)),
            padding=dp(10),
            spacing=dp(10)
        )

        # Controls title
        control_title = Label(
            text="Controls",
            font_size=dp(24),
            size_hint=(1, 0.1),
            font_name=FONT_PATH
        )
        self.controls.add_widget(control_title)

        # Control buttons
        start = Button(
            text="Start",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.play
        )
        pause = Button(
            text="Pause",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        step = Button(
            text="Move One Iteration",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1)
        )
        self.controls.add_widget(start)
        self.controls.add_widget(pause)
        self.controls.add_widget(step)

        # Spacer
        self.controls.add_widget(BoxLayout(size_hint=(1, 0.4)))

        # Add Controls to the Game Screen
        self.main_layout.add_widget(self.controls)

        # # Horizontal Spacer between controls and grid
        # self.main_layout.add_widget(BoxLayout(size_hint=(0.2, 0.4)))

        # Create grid container
        self.grid_container = GridLayout(
            size_hint=(None, None),
            size=(dp(856), dp(856)),
            padding=dp(20),
            rows=self.grid_size,
            orientation="lr-tb",
        )
        self.main_layout.add_widget(self.grid_container)

        # Create iteration label and generation label
        self.iteration_label = Label(text="Iteration: 1", font_size=dp(20), font_name=FONT_PATH)
        self.generation_label = Label(text="Generation: Blue", font_size=dp(20), font_name=FONT_PATH)

        self.populate_grid()
        self.print_grid()

        self.add_widget(self.main_layout)

    def populate_grid(self):
        cell_size = 5 # Original is 15
        placement = (800, 100)

        for i in range(self.grid_size):
            self.grid.append([])
            for j in range(self.grid_size):
                cell = Cell(
                    pos=(placement[0] + i*cell_size, placement[1] + j*cell_size),
                    size=(cell_size, cell_size),
                    color=(1, 0, 0, 1) if self.logic.main_matrix[i][j].get_state() == 1
                    else (0, 0, 0, 1)
                )
                self.grid[i].append(cell)
                self.grid_container.add_widget(cell)

    def play(self, *args):
        self.playing = True
        self.logic.update()
        self.update_grid()
        self.print_grid()
        current_iter = self.logic.iteration
        self.iteration_label.text = f"Iteration: {current_iter}"
        # Generation is blue if iteration is odd, else is red.
        self.generation_label.text = f'Generation: {"Blue" if current_iter % 2 == 1 else "Red" }'

    def update_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid[i][j].set_color(
                    (1, 0, 0, 1) if self.logic.main_matrix[i][j].get_state() == 1
                    else (0, 0, 0, 1)
                )

    def print_grid(self):
        print(self.grid)
        print()
        print("--- START AUTOMATON_KIVY ---")
        print("[*] Logic Grid: ")
        for i in range(self.grid_size):
            states = [self.logic.main_matrix[i][j].get_state() for j in range(self.grid_size)]
            print(states)
        print()
        print("[*] Graphical Grid: ")
        for i in range(self.grid_size):
            states = [1 if self.grid[i][j].color == [1, 0, 0, 1] else 0 for j in range(self.grid_size)]
            print(states)
        print()
        print("--- END AUTOMATON_KIVY ---")

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dimension = 100 # Original is 100
        self.logic = LogicManager(dimension=self.dimension, wraparound=False)
        gs = GameScreen(dimension=self.dimension, logic=self.logic)
        self.add_widget(gs)

kv = Builder.load_file("Automaton.kv")
Window.size = (1280, 896)

class AutomatonApp(App):
    def build(self):
        wm = WindowManager()
        return wm



if __name__ == "__main__":
    AutomatonApp().run()