from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from StartWindow import StartScreen

class AutomatonApp(App):
    def build(self):
        Window.size = (1080, 896)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        Window.set_title("Automaton")

        sm = ScreenManager()
        sm.add_widget(StartScreen(screen_manager=sm))  # Add StartScreen with layout
        return sm

if __name__ == '__main__':
    AutomatonApp().run()
