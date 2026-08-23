from html import entities

from Entity import Entity


class Game:
    def __init__(self):
        self.entities = []
        self.sizeX = 0
        self.sizeY = 0

    def Run(self, stdscr):
        self.InitGame(stdscr)
        self.UpdateGame(stdscr)

    def InitGame(self, stdscr):
        print('Willkommen bei PythonMan')

        self.sizeX = input('Wie breit soll das Feld werden?')
        self.sizeY = input('Wie hoch soll das Feld werden?')

        self.entities.append(Entity('c',self.sizeX / 2,self.sizeY / 2, '\033[33m'))

    def UpdateGame(self, stdscr):
        while True:
            for e in entities:
                e.Update(stdscr)