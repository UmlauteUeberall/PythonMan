from __future__ import annotations
from typing import TYPE_CHECKING

from Entities.Base.Drawable import Drawable

if TYPE_CHECKING:
    from Game import Game

class Wall(Drawable):
    def __init__(self, _game : Game, _posX : int, _posY : int):
        Drawable.__init__(self, _game, "█", "WHITE", _posX, _posY)
