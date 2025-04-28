from kivy.config import Config

# Set the initial window position BEFORE importing any UI modules
Config.set('graphics', 'position', 'custom')
Config.set('graphics', 'left', '100')   # X coordinate from the left of the screen
Config.set('graphics', 'top', '50')    # Y coordinate from the top of the screen

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from StartWindow import StartScreen

class AutomatonApp(App):
    def build(self):
        Window.size = (1280, 896)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        Window.set_title("Automaton")

        sm = ScreenManager()
        sm.add_widget(StartScreen(screen_manager=sm))  # Add StartScreen with layout
        return sm

if __name__ == '__main__':
    AutomatonApp().run()
