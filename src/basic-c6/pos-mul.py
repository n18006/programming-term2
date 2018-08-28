class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x2 = self.x + other.x
        y2 = self.y + other.y
        return Pos(x2, y2)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x2 = self.x * other
            y2 = self.y * other
            return Pos(x2, y2)
        else:
            raise TypeError

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

p1 = Pos(10, 20)
p2 = p1 * 1.7

print(p2)
