INF_POINT = None

class EllipticCurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p
        self.points = []
        self.definePoints()

    def definePoints(self):
        self.points.append(INF_POINT)
        for x in range(self.p):
            for y in range(self.p):
                if self.equalModp(y*y, x*x*x + self.a*x + self.b):
                    self.points.append((x, y))

    def numberPoints(self):
        return len(self.points)
    def discriminant(self):
        D = -16 * (4*self.a*self.a*self.a + 27*self.b*self.b)
        return self.reduceModp(D)

    def printPoints(self):
        print(self.points)

    def reduceModp(self, x):
        return x % self.p 
    def equalModp(self, x, y):
        return self.reduceModp(x - y) == 0

ec = EllipticCurve(2, 7, 19)
ec.printPoints()
print(ec.numberPoints())
print(ec.discriminant())