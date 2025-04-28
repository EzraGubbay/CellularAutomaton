from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.screenmanager import Screen
from AutomatonKivy import WindowManager  # Your logic manager
from ConfigScreen import ConfigScreen  # ✅ Make sure the file is named correctly
from AutomatonKivy import WindowManager  # Import from the correct file

class StartWindow(BoxLayout):
    def __init__(self, screen_manager, **kwargs):
        super(StartWindow, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [0, 0, 0, 0]
        self.spacing = 10
        self.screen_manager = screen_manager

        button_color = get_color_from_hex('#143D4B')

        button_layout = BoxLayout(
            orientation='vertical',
            size_hint=(None, None),
            spacing=15,
            width=400,
            height=400,
            pos_hint={'center_x': 0.5}
        )

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
        button_layout.add_widget(play)  # ← This line is missing!

        play.bind(on_press=self.open_game_screen)

        # Choose Configuration button
        config = Button(
            text='Choose Configuration',
            size_hint=(1, None),
            height=80,
            background_color=button_color,
            background_normal='',
            color=(1, 1, 1, 1)
        )
        config.bind(on_press=self.open_config_screen)
        button_layout.add_widget(config)

        self.add_widget(button_layout)
        self.add_widget(BoxLayout(size_hint=(1, 1)))  # Spacer

    def open_config_screen(self, instance):
        if not self.screen_manager.has_screen('config'):
            from ConfigScreen import ConfigScreen
            self.screen_manager.add_widget(ConfigScreen(name='config', screen_manager=self.screen_manager))

        self.screen_manager.transition.direction = 'left'  # Always reset direction
        self.screen_manager.current = 'config'
    
    def open_game_screen(self, instance):
        self.screen_manager.transition.direction = 'left'

        if not self.screen_manager.has_screen('game'):
            game_container = WindowManager()  # contains GameScreen already

            # Wrap it in a Screen
            game_screen_wrapper = Screen(name='game')
            game_screen_wrapper.add_widget(game_container)

            self.screen_manager.add_widget(game_screen_wrapper)

        self.screen_manager.current = 'game'

class StartScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.name = 'start'
        self.add_widget(StartWindow(screen_manager))
