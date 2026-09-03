from __future__ import annotations
from typing import TYPE_CHECKING
from Helper.Vector2 import Vector2

if TYPE_CHECKING:
    from Game import Game
import curses
from Entities.Base.Entity import Entity


class Drawable(Entity):
    def __init__(self, _game: Game, _symbol: str, _color: str, _pos: Vector2):
        Entity.__init__(self, _game, _pos)
        self.symbol: str = _symbol
        self.color: str = _color

    def Draw(self, _stdscr : curses.window):
        try:
            _stdscr.addstr(self.pos.Y, self.pos.X, self.symbol, curses.color_pair(self.game.colors[self.color]))
        except Exception:
            print(f"{self.pos.X} {self.pos.Y}")



