from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window

class ConfigScreen(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.name = 'config'
        self.screen_manager = screen_manager

        # Background color
        Window.clearcolor = (0.9, 0.9, 0.9, 1)
        button_color = get_color_from_hex('#143D4B')

        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        button_area = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1))
        button_column = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=6 * 95, spacing=15)

        for i in range(1, 6):
            btn = Button(
                text=f'Config {i}',
                size_hint=(1, None),
                height=80,
                background_color=button_color,
                background_normal='',
                color=(1, 1, 1, 1)
            )
            button_column.add_widget(btn)

        back = Button(
            text='Back',
            size_hint=(1, None),
            height=60,
            background_color=get_color_from_hex('#555555'),
            background_normal='',
            color=(1, 1, 1, 1)
        )
        #back.bind(on_press=lambda x: setattr(self.screen_manager, 'current', 'start'))
        def go_back(instance):
            self.screen_manager.transition.direction = 'right'
            self.screen_manager.current = 'start'

        back.bind(on_press=go_back)

        button_column.add_widget(back)

        button_area.add_widget(button_column)
        layout.add_widget(button_area)
        self.add_widget(layout)
