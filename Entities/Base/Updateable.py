from abc import ABC, abstractmethod
import curses

class Updatable:
    @abstractmethod
    def Update(self, _stdscr : curses.window) -> None:
        pass