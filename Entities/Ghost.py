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
        target : Vector2 = self.game.GetPlayerPos()
        direction : Vector2 = self.DonutDirection(target, self.game.size)
        if abs(direction.X) > abs(direction.Y):
            direction.Y = 0
        else:
            direction.X = 0

        if direction.SQRLength() == 0:
            return

        direction : Vector2 = direction / direction.Length()

        newPos : Vector2 = self.pos + direction
        newPos = newPos.Donut(self.game.size)

        if self.game.IsSpaceFree(newPos):
            self.pos = newPos

    def DonutDirection(self, other, size : Vector2) -> Vector2:
        direction : Vector2 = other - self.pos

        if abs(direction.X) > size.X / 2:
            if direction.X > 0:
                direction.X -= size.X
            else:
                direction.X += size.X

        if abs(direction.Y) > size.Y / 2:
            if direction.Y > 0:
                direction.Y -= size.Y
            else:
                direction.Y += size.Y

        return direction