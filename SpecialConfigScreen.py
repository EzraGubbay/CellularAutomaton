# SpecialConfigScreen.py
from kivy.uix.screenmanager import Screen
from LogicManager import LogicManager
from Automaton_Kivy import GameScreen

class SpecialConfigScreen(Screen):
    def load_ready_config(self, config_name, config_dict):
        config = config_dict[config_name]
        dimension = len(config)

        logic = LogicManager(dimension=dimension, wraparound=False, config=config)

        if 'game' in self.screen_manager.screen_names:
            self.screen_manager.remove_widget(self.screen_manager.get_screen('game'))

        game_screen = GameScreen(dimension=dimension, logic=logic)
        game_screen.name = 'game'
        self.screen_manager.add_widget(game_screen)
        self.screen_manager.current = 'game'
