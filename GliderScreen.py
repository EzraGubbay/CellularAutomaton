from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.utils import get_color_from_hex
from SpecialConfigurations import gliders
from SpecialConfigScreen import SpecialConfigScreen
from SpecialConfigurations import diagonal_gliders

class GliderScreen(SpecialConfigScreen):
    def __init__(self, screen_manager, wraparound=False, **kwargs):
        super().__init__(**kwargs)
        self.name = 'gliders'
        self.screen_manager = screen_manager
        self.wraparound = wraparound  # Set wraparound property
        button_color = get_color_from_hex('#143D4B')
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        button_area = AnchorLayout(anchor_x='center', anchor_y='top', size_hint=(1, 1))
        button_column = BoxLayout(orientation='vertical', size_hint=(None, None), width=400, height=550, spacing=15)
        for i in range(1, len(gliders) + 1):
            name = f'glider{i}'
            btn = Button(
                text=f'Glider {i}',
                size_hint=(1, None),
                height=80,
                background_color=button_color,
                background_normal='',
                color=(1, 1, 1, 1)
            )
            btn.bind(on_press=lambda instance, name=name: self.load_ready_config(name, diagonal_gliders))
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

    # def load_config(self, config_name):
    #     config = gliders[config_name]
    #     config_height = len(config)
    #     config_width = len(config[0])
    #     spacing = 2
    #     dimension = 50

    #     logic = LogicManager(dimension=dimension, wraparound=False)

    #     for i in range(dimension):
    #         for j in range(dimension):
    #             logic.main_matrix[i][j].set_state(0)

    #     max_tiles = min(
    #         (dimension - config_height) // (config_height + spacing) + 1,
    #         (dimension - config_width) // (config_width + spacing) + 1
    #     )

    #     for t in range(max_tiles):
    #         row_offset = t * (config_height + spacing)
    #         col_offset = t * (config_width + spacing)
    #         for y in range(config_height):
    #             for x in range(config_width):
    #                 logic.main_matrix[row_offset + y][col_offset + x].set_state(config[y][x])

    #     if 'game' in self.screen_manager.screen_names:
    #         self.screen_manager.remove_widget(self.screen_manager.get_screen('game'))

    #     game_screen = GameScreen(dimension=dimension, logic=logic)
    #     game_screen.name = 'game'
    #     self.screen_manager.add_widget(game_screen)
    #     self.screen_manager.current = 'game'

    def go_back(self, instance):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'config'
