import curses

from Entities.Base.Updateable import Updateable
from Entities.Base.Drawable import Drawable
from Entities.Pacman import Pacman
from Entities.Wall import Wall


class Game:
    def __init__(self):
        self.entities = []
        self.sizeX : int = 30
        self.sizeY : int = 15
        self.colors: dict[str, int] = {}

    def Run(self, stdscr : curses.window):
        self.InitGame(stdscr)
        self.UpdateGame(stdscr)

    def InitGame(self, stdscr: curses.window):
        curses.curs_set(0)
        curses.start_color()

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


        stdscr.addstr(0, 5, 'Willkommen bei PythonMan')

        stdscr.refresh()

        curses.napms(2000)

        for i in range(self.sizeX):
            self.AddEntity(Wall(self, i, 0))
            self.AddEntity(Wall(self, i, self.sizeY -1))

        for i in range(self.sizeY - 2):
            self.AddEntity(Wall(self, 0, i +1))
            self.AddEntity(Wall(self, self.sizeX - 1, i +1))


        self.AddEntity(Pacman(self, int(self.sizeX / 2), int (self.sizeY / 2)))



        #self.entities.append(Entity('c',self.sizeX / 2,self.sizeY / 2, '\033[33m'))

    def UpdateGame(self, stdscr: curses.window):
        while True:
            for e in self.entities:
                if isinstance(e, Updateable):
                    e.Update()


            stdscr.clear()
            for e in self.entities:
                if isinstance(e, Drawable):
                    e.Draw(stdscr)

            stdscr.refresh()
            curses.napms(100)


    def AddEntity(self, entity):
        self.entities.append(entity)

    def RemoveEntity(self, entity):
        self.entities.remove(entity)