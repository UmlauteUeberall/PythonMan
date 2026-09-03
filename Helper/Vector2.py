from __future__ import annotations

class Vector2:
    def __init__(self, _x, _y):
        self.X = _x
        self.Y = _y

    def __add__(self, other : Vector2):
        return Vector2(self.X + other.X, self.Y + other.Y)

    def __eq__(self, _o: Vector2) -> bool:
        return self.X == _o.X and self.Y == _o.Y

    def Donut(self, worldSize : Vector2) -> Vector2:
        return Vector2((self.X + worldSize.X) % worldSize.X, (self.Y + worldSize.Y) % worldSize.Y)

    def Length(self) -> float:
        return self.X * self.X + self.Y * self.Y