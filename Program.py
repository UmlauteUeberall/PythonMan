import curses

from ProgramState import ProgramState
from Scenes.BaseScene import BaseScene
from Scenes.Menu import Menu
from Scenes.Game import Game
from Scenes.Editor import Editor

class Program:

    def __init__(self):
        self.state : ProgramState = ProgramState.MENU
        self.isRunning = True

        self.scenes = {
            ProgramState.MENU : Menu(self),
            ProgramState.GAME : Game(self),
            ProgramState.EDITOR : Editor(self),
        }

    def Run(self, _stdscr : curses.window):
        # Cursor ausblenden
        curses.curs_set(0)
        # Farben erlauben
        curses.start_color()
        # Input non blocking
        _stdscr.nodelay(True)


        currentScene : BaseScene

        while self.isRunning:
            currentScene = self.scenes[self.state]

            currentScene.Run(_stdscr)

            currentScene.CleanUp()


