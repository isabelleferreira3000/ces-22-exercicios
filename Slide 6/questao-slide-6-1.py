class Shape:
    geometric_type = 'Generic Shape'

    def area(self):  # This acts as placeholder for the interface
        raise NotImplementedError

    def get_geometric_type(self):
        return self.geometric_type


class Plotter:

    def plot(self, ratio, topleft):
        # Imagine some nice plotting logic here...

        print('Plotting at {}, ratio {}.'.format(
            topleft, ratio))


class Polygon(Shape, Plotter):  # base class for polygons
    geometric_type = 'Polygon'


class RegularPolygon(Polygon):  # Is-A Polygon
    geometric_type = 'Regular Polygon'

    def __init__(self, side):
        self.side = side


class RegularHexagon(RegularPolygon): # Is-A Regular Polygon
    geometric_type = 'RegularHexagon'

    def area(self):
        return 1.5 * (3 ** .5 * self.side ** 2)


class Square(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'Square'

    def area(self):
        return self.side * self.side

class EquilateralTriangle(RegularPolygon): # Is-A RegularPolygon
    geometric_type = 'EquilateralTriangle'

    def area(self):
        return (self.side * self.side) * 1.73205 / 4


hexagon = RegularHexagon(10)
print(hexagon.area())
print(hexagon.get_geometric_type())
hexagon.plot(0.8, (75, 77))

square = Square(12)
print(square.area())
print(square.get_geometric_type())
square.plot(0.93, (74, 75))

triagle = EquilateralTriangle(5)
print(triagle.area())
print(triagle.get_geometric_type())
triagle.plot(0.5, (10, 20))

print(hexagon.__class__.mro())
print(square.__class__.mro())
print(triagle.__class__.mro())