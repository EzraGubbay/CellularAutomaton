from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from BlinkerScreen import BlinkerScreen
from GliderScreen import GliderScreen
from TrafficLightScreen import TrafficLightScreen


class ConfigScreen(Screen):
    def __init__(self, screen_manager, wraparound=False, **kwargs):
        super().__init__(**kwargs)
        self.name = 'config'
        self.wraparound = wraparound  # Set wraparound property
        self.screen_manager = screen_manager  # Set reference to the main screen manager

        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        button_color = get_color_from_hex('#143D4B')

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        button_area = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1))
        button_column = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=4 * 95, spacing=15)

        options = [
            ('Blinkers', 'blinkers'),
            ('Gliders', 'gliders'),
            ('Traffic Lights', 'traffic_lights'),
        ]

        for label, screen in options:
            btn = Button(
                text=label,
                size_hint=(1, None),
                height=80,
                background_color=button_color,
                background_normal='',
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda instance, scr=screen: self.go_to_screen(scr))
            button_column.add_widget(btn)

        back = Button(
            text='Back',
            size_hint=(1, None),
            height=60,
            background_color=get_color_from_hex('#555555'),
            background_normal='',
            color=(1, 1, 1, 1)
        )
        back.bind(on_press=self.go_back)
        button_column.add_widget(back)

        button_area.add_widget(button_column)
        layout.add_widget(button_area)
        self.add_widget(layout)

    def go_to_screen(self, screen_name):
        if screen_name == "blinkers" and "blinkers" not in self.screen_manager.screen_names:
            from BlinkerScreen import BlinkerScreen
            screen = BlinkerScreen(screen_manager=self.screen_manager,wraparound=self.wraparound)
            self.screen_manager.add_widget(screen)

        elif screen_name == "gliders" and "gliders" not in self.screen_manager.screen_names:
            from GliderScreen import GliderScreen
            screen = GliderScreen(screen_manager=self.screen_manager, wraparound=self.wraparound)
            self.screen_manager.add_widget(screen)

        elif screen_name == "traffic_lights" and "traffic_lights" not in self.screen_manager.screen_names:
            from TrafficLightScreen import TrafficLightScreen
            screen = TrafficLightScreen(screen_manager=self.screen_manager, wraparound=self.wraparound)
            self.screen_manager.add_widget(screen)

        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = screen_name


    def go_back(self, instance):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'start'
