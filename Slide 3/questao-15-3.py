class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y

    def slope_from_origin(self):
        if self.x != 0:
            result = self.y/self.x
        elif self.y > 0:
            result = "mais infinito"
        elif self.y < 0:
            result = "menos infinito"
        else:
            result = "indeterminado"
        print(result)
        return result


Point(4, 10).slope_from_origin()
Point(4, 2).slope_from_origin()
Point(0, 10).slope_from_origin()  # o método falharia quando x fosse zero
Point(4, 0).slope_from_origin()
Point(0, 0).slope_from_origin()  # o método também falharia quando x e y fossem zero
