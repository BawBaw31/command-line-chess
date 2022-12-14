
from enum import Enum

from Map import Map


class GameStates(Enum):
    MAIN_MENU = 1
    GAME = 2
    PAUSE = 3
    SETTINGS = 4


class GameManager:
    state: GameStates = GameStates.GAME
    map: Map = Map()

    def __init__(self):
        self.game_loop()

    def game_loop(self):
        if self.state == GameStates.MAIN_MENU:
            self.main_menu()
        elif self.state == GameStates.GAME:
            self.game()
        elif self.state == GameStates.PAUSE:
            self.pause()
        elif self.state == GameStates.SETTINGS:
            self.settings()

    def main_menu(self):
        pass

    def game(self):
        self.map.render()
        input()

    def pause(self):
        pass

    def settings(self):
        pass
