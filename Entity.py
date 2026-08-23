class Entity:
    def __init__(self, _symbol, _posX, _posY, _color):
        self.position = (_posX, _posY)
        self.symbol = _symbol
        self.color = _color

        def Update(stdscr):
            print(self.symbol)