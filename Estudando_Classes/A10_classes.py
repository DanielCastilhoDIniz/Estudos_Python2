class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print(self.x, self.y)


a = Point(0, 0)
b = Point(0, 1)

a.print_point()
b.print_point()
