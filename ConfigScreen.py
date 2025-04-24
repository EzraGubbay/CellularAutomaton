from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from SpecialConfigurations import blinkers
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
            blinker_name = f'blinker{i}'
            btn = Button(
                text=f'Config {i}',
                size_hint=(1, None),
                height=80,
                background_color=button_color,
                background_normal='',
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda instance, name=blinker_name: self.load_config(name))
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
    
    #import random  # Needed for random cell initialization

    def load_config(self, config_name):
        config = blinkers[config_name]
        config_height = len(config)
        config_width = len(config[0])
        spacing = 1
        dimension = 50

        from LogicManager import LogicManager
        logic = LogicManager(dimension=dimension, wraparound=False)

        #step 1: Initialize the main matrix with cells as 0s
        for i in range(dimension):
            for j in range(dimension):
                logic.main_matrix[i][j].set_state(0)
        # Step 2: Place blinkers on the diagonal (overwrite random cells)
        max_tiles = min(
            (dimension - config_height) // (config_height + spacing) + 1,
            (dimension - config_width) // (config_width + spacing) + 1
        )

        for t in range(max_tiles):
            row_offset = t * (config_height + spacing)
            col_offset = t * (config_width + spacing)

            for y in range(config_height):
                for x in range(config_width):
                    logic.main_matrix[row_offset + y][col_offset + x].set_state(config[y][x])

        from Automaton_Kivy import GameScreen

        if 'game' in self.screen_manager.screen_names:
            self.screen_manager.remove_widget(self.screen_manager.get_screen('game'))

        game_screen = GameScreen(dimension=dimension, logic=logic)
        game_screen.name = 'game'
        self.screen_manager.add_widget(game_screen)
        self.screen_manager.current = 'game'
