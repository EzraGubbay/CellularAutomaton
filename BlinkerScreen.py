from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex
from SpecialConfigurations import blinkers
from SpecialConfigScreen import SpecialConfigScreen
from SpecialConfigurations import diagonal_blinkers

class BlinkerScreen(SpecialConfigScreen):
    def __init__(self, screen_manager, wraparound=False,**kwargs):
        super().__init__(**kwargs)
        self.name = 'blinkers'
        self.wraparound = wraparound  # Set wraparound property
        self.screen_manager = screen_manager
        button_color = get_color_from_hex('#143D4B')
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        button_area = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1))
        button_column = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=550, spacing=15)

        for i in range(1, len(blinkers) + 1):
            name = f'blinker{i}'
            btn = Button(
                text=f'Blinker {i}',
                size_hint=(1, None),
                height=80,
                background_color=button_color,
                background_normal='',
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda instance, name=name: self.load_ready_config(name, diagonal_blinkers))
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

    def go_back(self, instance):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'config'
