from __future__ import annotations
from typing import TYPE_CHECKING

from Entities.Base.Drawable import Drawable
from Entities.Base.Updateable import Updateable

import random

if TYPE_CHECKING:
    from Game import Game
class Pacman(Drawable, Updateable):
    def __init__(self, _game : Game, _posX : int, _posY : int):
        Drawable.__init__(self, _game,"O", "YELLOW", _posX, _posY)
        Updateable.__init__(self)

    def Update(self):
        self.posX += random.randint(-1, 1)
        self.posY += random.randint(-1, 1)

        self.posX = (self.posX + self.game.sizeX) % self.game.sizeX
        self.posY = (self.posY + self.game.sizeY) % self.game.sizeY
