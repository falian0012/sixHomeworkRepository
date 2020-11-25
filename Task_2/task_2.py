class Road:
    _length = 0
    _width = 0

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def calc_weight(self):
        return self._length * self._width * 25 * 0.05

road = Road(20, 5000)
print(road.calc_weight())