from __future__ import annotations
from typing import TYPE_CHECKING
from Entities.Base.Solid import Solid

from Entities.Base.Drawable import Drawable
from Helper.Vector2 import Vector2

if TYPE_CHECKING:
    from Scenes.Game import Game

class Wall(Drawable, Solid):
    def __init__(self, _game : Game, _pos : Vector2):
        Drawable.__init__(self, _game, "█", "WHITE", _pos)
