from __future__ import annotations
from typing import TYPE_CHECKING
from Entities.Base.Collectable import Collectable

from Entities.Base.Drawable import Drawable
from Helper.Vector2 import Vector2

if TYPE_CHECKING:
    from Game import Game

class Coin(Drawable, Collectable):
    def __init__(self, _game : Game, _pos : Vector2):
        Drawable.__init__(self, _game, "•", "GREEN", _pos)
        Collectable.__init__(self, 10)
