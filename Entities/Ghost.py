from __future__ import annotations
from typing import TYPE_CHECKING
from Helper.Vector2 import Vector2

from Entities.Base.Drawable import Drawable
from Entities.Base.Updateable import Updatable

import curses
import random

if TYPE_CHECKING:
    from Scenes.Game import Game
class Ghost(Drawable, Updatable):
    def __init__(self, _game: Game, _pos: Vector2, _color : str):
        Drawable.__init__(self, _game, "X", _color, _pos)
        Updatable.__init__(self)

    def Update(self, _stdscr):

        x = random.randint(1, 4)
        delta: Vector2 = Vector2(0, 0)
        if x == 1:
            delta.Y = -1
        elif x == 2:
            delta.Y = 1
        elif x == 2:
            delta.X = -1
        elif x == 3:
            delta.X = 1

        if delta.SQRLength() == 0:
            return

        newPos = self.pos + delta
        newPos = newPos.Donut(self.game.size)

        if self.game.IsSpaceFree(newPos):
            self.pos = newPos
