from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Game import Game

class Entity:
    def __init__(self, _game : Game, _posX: int, _posY: int):
        self.game = _game
        self.posX: int = _posX
        self.posY: int = _posY
