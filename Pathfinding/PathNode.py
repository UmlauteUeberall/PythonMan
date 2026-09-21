from Helper.Vector2 import Vector2

class PathNode:
    def __init__(self, _pos : Vector2):
        self.pos : Vector2 = _pos
        self.neighbours : List[PathNode] = []

    def AddNeighbour(self, _neighbour : PathNode):
        self.neighbours.append(_neighbour)


    def Reset(self):
        pass