from __future__ import annotations
from typing import TYPE_CHECKING

from Entities.Base.Drawable import Drawable
from Entities.Base.Updateable import Updateable

import curses

if TYPE_CHECKING:
    from Game import Game
class Pacman(Drawable, Updateable):
    def __init__(self, _game : Game, _posX : int, _posY : int):
        Drawable.__init__(self, _game,"O", "YELLOW", _posX, _posY)
        Updateable.__init__(self)

    def Update(self, _stdscr):

        key = _stdscr.getch()
        deltaX : int = 0
        deltaY : int = 0
        if key == curses.KEY_UP:
            deltaY = -1
        elif key == curses.KEY_DOWN:
            deltaY = 1
        elif key == curses.KEY_LEFT:
            deltaX = -1
        elif key == curses.KEY_RIGHT:
            deltaX = 1

        self.posX += deltaX
        self.posY += deltaY

        self.posX = (self.posX + self.game.sizeX) % self.game.sizeX
        self.posY = (self.posY + self.game.sizeY) % self.game.sizeY
