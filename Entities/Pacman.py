from __future__ import annotations
from typing import TYPE_CHECKING
from Helper.Vector2 import Vector2

from Entities.Base.Drawable import Drawable
from Entities.Base.Updateable import Updatable

import curses

if TYPE_CHECKING:
    from Scenes.Game import Game
class Pacman(Drawable, Updatable):
    def __init__(self, _game : Game, _pos : Vector2):
        Drawable.__init__(self, _game,"O", "YELLOW", _pos)
        Updatable.__init__(self)

    def Update(self, _stdscr):

        delta : Vector2  = Vector2(0,0)
        if self.game.currentKey == curses.KEY_UP:
            delta.Y = -1
        elif self.game.currentKey == curses.KEY_DOWN:
            delta.Y = 1
        elif self.game.currentKey == curses.KEY_LEFT:
            delta.X = -1
        elif self.game.currentKey == curses.KEY_RIGHT:
            delta.X = 1

        if delta.Length() == 0:
            return

        newPos = self.pos + delta
        newPos = newPos.Donut(self.game.size)

        if self.game.IsSpaceFree(newPos):
            self.pos = newPos
            self.game.Collect(newPos)

