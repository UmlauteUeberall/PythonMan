import curses
import time

from Entities.Base.Collectable import Collectable
from Entities.Base.Updateable import Updatable
from Entities.Base.Drawable import Drawable
from Entities.Coin import Coin
from Entities.Pacman import Pacman
from Entities.Wall import Wall
from Helper.Vector2 import Vector2
from Entities.Base.Solid import Solid


class Game:
    def __init__(self):
        self.entities = []
        self.size : Vector2 = Vector2(30, 20)
        self.colors: dict[str, int] = {}
        self.startTime : float = time.monotonic()
        self.frameCounter : int = 0
        self.score : int = 0

    def Run(self, _stdscr : curses.window):
        self.InitGame(_stdscr)
        self.UpdateGame(_stdscr)

    def InitGame(self, _stdscr: curses.window):
        # Cursor ausblenden
        curses.curs_set(0)
        # Farben erlauben
        curses.start_color()
        # Input non blocking
        _stdscr.nodelay(True)

        self.colors["RED"] = 1
        self.colors["GREEN"] = 2
        self.colors["YELLOW"] = 3
        self.colors["BLUE"] = 4
        self.colors["WHITE"] = 5

        curses.init_pair(self.colors["RED"], curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(self.colors["GREEN"], curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(self.colors["YELLOW"], curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(self.colors["BLUE"], curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(self.colors["WHITE"], curses.COLOR_WHITE, curses.COLOR_BLACK)

        _stdscr.addstr(0, 5, 'Willkommen bei PythonMan')

        _stdscr.refresh()

        curses.napms(2000)

        for i in range(self.size.X):
            if i != (self.size.X - 2) / 2:
                self.AddEntity(Wall(self, Vector2( i, 0)))
                self.AddEntity(Wall(self, Vector2( i, self.size.Y -1)))

        for i in range(self.size.Y - 2):
            if i != (self.size.Y -2)  / 2:
                self.AddEntity(Wall(self, Vector2( 0, i +1)))
                self.AddEntity(Wall(self, Vector2(self.size.X - 1, i +1)))

        for x in range(self.size.X):
            for y in range(self.size.Y):
                if self.IsSpaceFree(Vector2(x, y)) and not( x == int(self.size.X / 2) and y == int(self.size.Y / 2)):
                    self.AddEntity(Coin(self, Vector2(x, y)))

        self.AddEntity(Pacman(self, Vector2(int(self.size.X / 2), int (self.size.Y / 2))))

    def UpdateGame(self, _stdscr: curses.window):
        while True:
            for e in self.entities:
                if isinstance(e, Updatable):
                    e.Update(_stdscr)

            curses.flushinp()

            _stdscr.clear()
            for e in self.entities:
                if isinstance(e, Drawable):
                    e.Draw(_stdscr)

            self.DrawInfo(_stdscr)

            _stdscr.refresh()
            curses.napms(100)

    def DrawInfo(self, _stdscr: curses.window):
        InfoX = self.size.X + 2

        _stdscr.addstr(1, InfoX, f"Frames:          {self.frameCounter}")
        self.frameCounter += 1

        elapsed = int(time.monotonic() - self.startTime)
        minutes = elapsed // 60
        seconds = elapsed % 60
        _stdscr.addstr(2, InfoX, f"Passed Time:     {minutes:02}:{seconds:02}")

        _stdscr.addstr(3, InfoX, f"Score:           {self.score}")

    def AddEntity(self, _entity):
        self.entities.append(_entity)

    def RemoveEntity(self, _entity):
        self.entities.remove(_entity)

    def IsSpaceFree(self, pos: Vector2) -> bool:
        for e in self.entities:
            if isinstance(e, Solid) and e.pos == pos:
                return False
        return True

    def Collect(self, pos: Vector2):
        for e in self.entities:
            if isinstance(e, Collectable) and e.pos == pos:
                self.score += e.score
                self.RemoveEntity(e)
