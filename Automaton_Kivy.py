from kivy.app import App
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import Clock
from kivy.graphics import Color, Rectangle, Line

from LogicManager import LogicManager
import SpecialConfigurations

FONT_PATH = "Fonts/Montserrat-Medium.ttf"

class Grid(Widget):
    def __init__(self, dimension: int, logic: LogicManager, cell_size: int=16, **kwargs):
        super().__init__(**kwargs)
        self.dimension = dimension
        self.logic = logic
        self.cell_size = cell_size

        # Offsets for placing the grid in the correct position
        self.offset_x = 500
        self.offset_y = 50

        # Grid dimensions *in pixels* based on cell size
        self.grid_width = self.dimension * self.cell_size

        # If a grid dimension is larger than 50, use batch optimization.
        # By default, grid size is 100, therefore this is generally true.
        self.is_large = self.dimension > 50

        # Render initial grid
        self.render_canvas()

    def render_canvas(self):
        self.canvas.clear()

        with self.canvas:
            # Background color
            Color(0.95, 0.95, 0.95, 1)
            Rectangle(pos=(self.offset_x, self.offset_y), size=(self.grid_width, self.grid_width))

            # Save cells based on state for batch drawing
            red_cells = []
            black_cells = []

            # Sort black and red cells into respective lists.
            for i in range(self.dimension):
                for j in range(self.dimension):
                    state = self.logic.main_matrix[i][j].get_state()

                    # Get coordinates of graphical square
                    x = i * self.cell_size + self.offset_x
                    y = j * self.cell_size + self.offset_y

                    # If the cell is meant to be red save in red_cells, otherwise black_cells.
                    if state == 1:
                        red_cells.append((x, y))
                    else:
                        black_cells.append((x, y))

            # Batch draw all black cells
            if black_cells:
                Color(0, 0, 0, 1) # Change drawing color to black
                for x, y in black_cells:
                    Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))

            # Batch draw all red cells
            if red_cells:
                Color(1, 0, 0, 1)  # Change drawing color to red
                for x, y in red_cells:
                    Rectangle(pos=(x, y), size=(self.cell_size, self.cell_size))

            # Draw cell borders:
            Color(0.4, 0.4, 0.4, 1) # Change to dark gray

            Line(rectangle=(self.offset_x, self.offset_y, self.grid_width, self.grid_width), width=2)

            for i in range(self.dimension):
                x = i * self.cell_size + self.offset_x
                y = i * self.cell_size + self.offset_y
                Line(points=[x, self.offset_y, x, self.offset_y + self.grid_width], width=1)
                Line(points=[self.offset_x, y, self.offset_x + self.grid_width, y], width=1)



class GameScreen(Screen):
    def __init__(self, dimension: int, logic: LogicManager, **kwargs):
        super().__init__(**kwargs)

        self.grid_size = dimension
        self.logic = logic
        self.playing = False

        self.main_layout = BoxLayout(orientation="horizontal", spacing=dp(10))

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
            font_name=FONT_PATH,
            color=(0, 0, 0, 1) # Black
        )
        self.controls.add_widget(control_title)

        # Control buttons
        self.start = Button(
            text="Start",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1),
            on_press=self.play
        )
        self.pause = Button(
            text="Pause",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1),
            on_press=self.toggle_pause,
            disabled=True
        )

        self.step = Button(
            text="Move One Iteration",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1),
            on_press=lambda _: Clock.schedule_once(self.iteration)
        )

        self.back = Button(
            text="Return to Main Menu",
            size_hint=(1, 0.08),
            background_color=(0.2, 0.6, 0.8, 1),
            on_release=self.return_to_main_menu
        )

        self.controls.add_widget(self.start)
        self.controls.add_widget(self.pause)
        self.controls.add_widget(self.step)
        self.controls.add_widget(self.back)

        # Spacer
        self.controls.add_widget(BoxLayout(size_hint=(1, 0.4)))

        # Add Controls to the Game Screen
        self.main_layout.add_widget(self.controls)

        # Create grid container
        self.grid_container = BoxLayout(
            size_hint=(None, None),
            size=(dp(856), dp(856)),
            padding=dp(20)
        )

        cell_size = 16 # Original is 16
        self.grid = Grid(dimension=self.grid_size, logic=self.logic, cell_size=cell_size)
        self.grid_container.add_widget(self.grid)
        self.main_layout.add_widget(self.grid_container)

        # Create labels for iteration number, generation and metrics
        self.iteration_label = Label(text="Iteration: 1", font_size=dp(20), font_name=FONT_PATH, color=(0, 0, 0, 1))
        self.generation_label = Label(text="Generation: Blue", font_size=dp(20), font_name=FONT_PATH, color=(0, 0, 0, 1))
        self.alive_label = Label(text=f'Alive Cells (Red):\n{self.logic.get_alive_cells()}', font_size=dp(20), font_name=FONT_PATH, color=(0, 0, 0, 1))
        self.labels = BoxLayout(orientation="vertical", size_hint=(1, 0.4), spacing=dp(5), pos_hint={"center_y": 0.8})
        self.labels.add_widget(self.iteration_label)
        self.labels.add_widget(self.generation_label)
        self.labels.add_widget(self.alive_label)
        self.main_layout.add_widget(self.labels)

        self.add_widget(self.main_layout)

    def play(self, *args):
        self.start.disabled = True
        self.pause.disabled = False
        self.step.disabled = True
        self.playing = True
        Clock.schedule_interval(self.iteration, 1.0 / 2.0)

    def iteration(self, dt):
        self.logic.update()
        self.grid.render_canvas()
        self.update_labels()

        # If user paused or stopped the game for some reason, stop iterating.
        if not self.playing or self.logic.iteration >= 250:
            Clock.unschedule(self.iteration)

    def update_labels(self):
        current_iter = self.logic.iteration
        self.iteration_label.text = f"Iteration: {current_iter}"
        # Generation is blue if iteration is odd, else is red.
        self.generation_label.text = f'Generation: {"Blue" if current_iter % 2 == 1 else "Red"}'
        self.alive_label.text = f'Alive Cells (Red):\n{self.logic.get_alive_cells()}'

    def toggle_pause(self, *args):
        if self.playing:
            self.playing = False
            self.pause.text = 'Resume'
            self.step.disabled = False
        else:
            self.playing = True
            self.pause.text = 'Pause'
            self.step.disabled = True
            Clock.schedule_interval(self.iteration, 1.0 / 2.0)

    def return_to_main_menu(self, instance):
        self.manager.transition.direction = 'right'
        self.manager.current = 'start'
        self.manager.remove_widget(self)

class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dimension = 10 # Original is 100
        self.logic = LogicManager(dimension=self.dimension, wraparound=False, config=None)
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
