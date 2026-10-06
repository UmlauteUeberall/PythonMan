from Helper.Vector2 import Vector2

class PathNode:
    def __init__(self, _pos : Vector2):
        self.pos : Vector2 = _pos
        self.walkable = True

    def Reset(self):
        self.walkable = True
