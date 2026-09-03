from __future__ import annotations
from typing import TYPE_CHECKING
from Helper.Vector2 import Vector2

if TYPE_CHECKING:
    from Game import Game

class Entity:
    def __init__(self, _game : Game, _pos: Vector2):
        self.game = _game
        self.pos: Vector2 = _pos
