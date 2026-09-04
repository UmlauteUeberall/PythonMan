
from __future__ import annotations

import curses

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod


if TYPE_CHECKING:
    from Program import Program

class BaseScene:
    def __init__(self, _program : Program):
        self.isRunning = False
        self.program = _program

    @abstractmethod
    def CleanUp(self) -> None:
        pass

    @abstractmethod
    def Run(self, _stdscr: curses.window) -> None:
        pass