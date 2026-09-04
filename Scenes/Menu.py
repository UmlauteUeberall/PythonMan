from __future__ import annotations

from typing import TYPE_CHECKING

from ProgramState import ProgramState

if TYPE_CHECKING:
    from Program import Program

import curses
from Scenes.BaseScene import BaseScene

class Menu(BaseScene):

    def __init__(self, _program: Program):
        BaseScene.__init__(self, _program)

        self.currentKey : int = 0

    def Run(self, _stdscr : curses.window):
        self.InitMenu(_stdscr)
        self.UpdateMenu(_stdscr)

    def InitMenu(self, _stdscr : curses.window):
        self.isRunning = True

        curses.flushinp()
        _stdscr.erase()

        _stdscr.addstr(5, 5, 'Welcome to PythonMan')
        _stdscr.refresh()

        curses.napms(1000)

    def UpdateMenu(self, _stdscr : curses.window):
        while self.isRunning:
            self.currentKey = _stdscr.getch()

            curses.flushinp()
            _stdscr.erase()

            _stdscr.addstr(5, 5, 'Press S to start')
            _stdscr.addstr(6, 5, 'Press Q to quit')

            if self.currentKey == 113:      # q
                self.isRunning = False
                self.program.isRunning = False
            if self.currentKey == 115:  # s
                self.isRunning = False
                self.program.state = ProgramState.GAME

            _stdscr.noutrefresh()
            curses.doupdate()

            curses.napms(100)


    def CleanUp(self):
        pass