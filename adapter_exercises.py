class LegacyRectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def __str__(self):
        return f'(x, y): ({self.x}, {self.y}), width: {self.width}, height: {self.height}'


class NewRectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def __str__(self):
        return f'(x1, y1): ({self.x1}, {self.y1}), (x2, y2): ({self.x2}, {self.y2})'


class RectangleAdapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_new_rectangle(self):
        x1 = self.adaptee.x
        y1 = self.adaptee.y
        x2 = self.adaptee.x + self.adaptee.width
        y2 = self.adaptee.y - self.adaptee.height
        return NewRectangle(x1, y1, x2, y2)


rect1 = NewRectangle(1, 2, 3, 4)
rect2 = LegacyRectangle(1, 2, 2, 2)
adapter = RectangleAdapter(rect2)
new_rect = adapter.get_new_rectangle()
print(rect1)
print(rect2)
print(new_rect)
