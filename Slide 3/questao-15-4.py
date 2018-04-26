class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def get_line_to(self, point):
        if point.x != self.x:
            result = ((point.y - self.y)/(point.x - self.x),
                      (self.y * point.x - self.x * point.y)/(point.x - self.x))
        else:
            result = "reta vertical"
        return result


print(Point(4, 11).get_line_to(Point(6, 15)))
print(Point(4, 11).get_line_to(Point(4, 15)))  # o método falharia qndo as abiscisas fossem iguais para os dois pontos
