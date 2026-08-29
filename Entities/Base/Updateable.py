from abc import ABC, abstractmethod
import curses

class Updateable:
    @abstractmethod
    def Update(self, _stdscr : curses.window) -> None:
        pass