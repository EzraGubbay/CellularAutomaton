from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class StartWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(StartWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0, 0, 0, 0]
        self.spacing = 10

        button_color = get_color_from_hex('#143D4B')

        button_layout = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            spacing=15
        )
        button_layout.width = 400
        button_layout.height = 400
        button_layout.pos_hint = {'center_x': 0.5}

        # Wrap around toggle button
        self.wrap_around_active = False
        self.wrap_around_button = Button(
            text='Wrap Around: Off',
            size_hint=(1, None),
            height=80,
            background_color=button_color,
            background_normal='',
            color=(1, 1, 1, 1)
        )

        def toggle_wrap_around(instance):
            self.wrap_around_active = not self.wrap_around_active
            if self.wrap_around_active:
                instance.text = 'Wrap Around: On'
                # Lighter color when active
                instance.background_color = [min(c * 1.3, 1) for c in button_color[:3]] + [1]
            else:
                instance.text = 'Wrap Around: Off'
                instance.background_color = button_color

        self.wrap_around_button.bind(on_press=toggle_wrap_around)
        button_layout.add_widget(self.wrap_around_button)

        # Play button
        play = Button(
            text='Play',
            size_hint=(1, None),
            height=80,
            background_color=button_color,
            background_normal='',
            color=(1, 1, 1, 1)
        )
        button_layout.add_widget(play)

        # Choose configuration button
        choseConfig = Button(
            text='Choose Configuration',
            size_hint=(1, None),
            height=80,
            background_color=button_color,
            background_normal='',
            color=(1, 1, 1, 1)
        )
        button_layout.add_widget(choseConfig)

       # self.add_widget(BoxLayout(size_hint=(1, 1)))  # Spacer at top
        self.add_widget(button_layout)
        self.add_widget(BoxLayout(size_hint=(1, 1)))  # Spacer at bottom

class StartApp(App):
    def build(self):
        Window.size = (1080, 896)
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        Window.set_title("Automaton")
        return StartWindow()

if __name__ == '__main__':
    StartApp().run()
