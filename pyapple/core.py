class Vector:
    __slots__ = ['x', 'y']

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
        else:
            raise NotImplemented
