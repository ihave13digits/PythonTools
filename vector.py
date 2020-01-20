#!/usr/bin/python3

class Vector2:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, i):
        return Vector2((self.x + i.x),(self.y + i.y))

    def __sub__(self, i):
        return Vector2((self.x - i.x),(self.y - i.y))

    def __mul__(self, i):
        return Vector2((self.x * i.x),(self.y * i.y))

    def __div__(self, i):
        return Vector2((self.x / i.x),(self.y / i.y))

    def coords(self):
        return Vector2(self.x, self.y)