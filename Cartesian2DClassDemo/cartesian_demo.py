#### Name: Grace Hadiyanto
#### E-mail: ifoundparis@gmail.com
#### CS223P
#### Assignment 3

from math import sqrt

class Cartesian2D:
    """ A class that defines a pair of coordinates in a 2D plane.
    Supported methods between 2 pairs of coordinates are addition, subtraction,
    comparison, and finding the distance in between.
    Supported methods for one pair of coordinates are multiplication, finding 
    length, and normalizing."""

    __slots__ = { '_x', '_y' }

    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    # The 'x' property
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    
    # The 'y' property
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, value):
        self._y = value

    # Method to be called on floating numbers after an operation to set their
    # precision to the hundredths place.
    def setPrecision(self, num):
        return round(num, 2)

    def distanceTo(self, v):
        return self.setPrecision(sqrt((v.x - self.x)**2 + (v.y - self.y)**2))

    def __add__(self, v):
        return Cartesian2D(self.setPrecision(self.x + v.x), 
                           self.setPrecision(self.y + v.y))
    
    def __repr__(self):
        return 'Cartesian2D({0.x:0.2f},{0.y:0.2f})'.format(self)

    def __sub__(self, v):
        return Cartesian2D(self.setPrecision(self.x - v.x), 
                           self.setPrecision(self.y - v.y))

    def __eq__(self, v):
        return (self.x == v.x and self.y == v.y)
    
    def __mul__(self, n):
        return Cartesian2D(self.setPrecision(self.x * n), 
                           self.setPrecision(self.y * n))

    def length(self):
        return self.setPrecision(sqrt(self.x**2 + self.y**2))

    def normalize(self):
        return Cartesian2D(self.x / self.length(), self.y / self.length())

# Returns the dot product of 2 instances of a Cartesian2D object  
def dot(v1, v2):
    return '{0:.2f}'.format((v1.x * v2.x) + (v1.y * v2.y))


def main():
    
    a = Cartesian2D(2.3, 3.4)
    b = Cartesian2D(4.5, 1.8)
    c = Cartesian2D(8.1, 0.3)
    print("The distance from a to b is {}".format(a.distanceTo(b)))
    print("The distance from b to c is {}".format(b.distanceTo(c)))
    d = a + b
    print("a + b = ({},{})".format(d.x, d.y))
    d = c - b
    print("c - b = ({}, {})".format(d.x, d.y))
    print("The length of a is {}".format(a.length()))
    print("The length of b is {}".format(b.length()))
    print("The length of c is {}".format(c.length()))
    # the normalize method returns a unit length vector
    unita = a.normalize()
    unitb = b.normalize()
    unitc = c.normalize()
    print("The length of unit a is {}".format(unita.length()))
    print("The length of unit b is {}".format(unitb.length()))
    print("The length of unit c is {}".format(unitc.length()))
    if a == b:
        print('Somehow a is equal to b?')
    else:
        print('a is not equal to b')
    s = 4
    d = unita * s
    print(d)
    print("The length of d is {}".format(d.length()))
    e = unitb * s
    f = dot(a, b)
    g = dot(unita, unitb)
    h = dot(d, e)
    print("dot(a, b) = {}".format(f))
    print("dot(unita, unitb) = {}".format(g))
    print("dot(d, e) = {}".format(h))

    
if __name__ == '__main__':
    main()
