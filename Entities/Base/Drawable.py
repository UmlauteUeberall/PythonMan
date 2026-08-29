from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Game import Game
import curses
from Entities.Base.Entity import Entity


class Drawable(Entity):
    def __init__(self, _game: Game, _symbol: str, _color: str, _posX: int, _posY: int):
        Entity.__init__(self, _game, _posX, _posY)
        self.symbol: str = _symbol
        self.color: str = _color

    def Draw(self, stdscr):
        try:
            stdscr.addstr(self.posY, self.posX, self.symbol, curses.color_pair(self.game.colors[self.color]))
        except Exception:
            print(f"{self.posX} {self.posY}")



