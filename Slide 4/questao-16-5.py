class Point:
    """ Create a new Point, at coordinates x, y """

    def __init__(self, x=0, y=0):
        """ Create a new point at x, y """
        self.x = x
        self.y = y


class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def inside_rectangle(self, point):
        if point.x >= self.corner[0]:
            if point.x <= self.corner[0] + self.width:
                if point.y <= self.corner[1]:
                    if point.y >= self.corner[1] - self.height:
                        return True
        return False

    def collision_detection(self, rectangle):
        corner_left_up = Point(rectangle.corner[0], rectangle.corner[1])
        corner_right_up = Point(rectangle.corner[0] + rectangle.width, rectangle.corner[1])
        corner_right_down = Point(rectangle.corner[0] + rectangle.width, rectangle.corner[1] - rectangle.height)
        corner_left_down = Point(rectangle.corner[0], rectangle.corner[1] - rectangle.height)

        corners = [corner_left_up, corner_right_up, corner_right_down, corner_left_down]

        for i in corners:
            if self.inside_rectangle(i):
                return True
        return False


rect_1 = Rectangle((0, 0), 10, 20)
rect_2 = Rectangle((5, -10), 10, 20)
rect_3 = Rectangle((-5, -10), 10, 20)
rect_4 = Rectangle((-5, 10), 10, 20)
rect_5 = Rectangle((5, 10), 10, 20)
rect_6 = Rectangle((5, 15), 10, 5)

print(rect_1.collision_detection(rect_2))
print(rect_1.collision_detection(rect_3))
print(rect_1.collision_detection(rect_4))
print(rect_1.collision_detection(rect_5))
print(rect_1.collision_detection(rect_6))
