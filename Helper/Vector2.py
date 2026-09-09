from __future__ import annotations

from math import sqrt

class Vector2:
    def __init__(self, _x : int, _y : int):
        self.X : int = _x
        self.Y : int = _y

    def __add__(self, other : Vector2):
        return Vector2(self.X + other.X, self.Y + other.Y)

    def __sub__(self, other : Vector2):
        return Vector2(self.X - other.X, self.Y - other.Y)

    def __mul__(self, other : int) -> Vector2:
        return Vector2(self.X * other, self.Y * other)

    def __truediv__(self, other : int) -> Vector2:
        return Vector2(int(round(self.X / other)), int(round(self.Y / other)))

    def __eq__(self, _o: Vector2) -> bool:
        return self.X == _o.X and self.Y == _o.Y

    def Donut(self, worldSize : Vector2) -> Vector2:
        return Vector2((self.X + worldSize.X) % worldSize.X, (self.Y + worldSize.Y) % worldSize.Y)

    def SQRLength(self) -> int:
        return self.X * self.X + self.Y * self.Y

    def Length(self) -> int:
        return int(round(sqrt(self.X * self.X + self.Y * self.Y)))