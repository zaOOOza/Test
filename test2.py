import unittest
from main import Coordinates, line_length


class TestLineLength(unittest.TestCase):

    def test_point1(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(1, 1)
        self.assertEqual(2.8284271247461903, line_length(point_1, point_2))

    def test_point2(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(5, 5)
        self.assertEqual(2.8284271247461903, line_length(point_1, point_2))

    def test_point3(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(1, 5)
        self.assertEqual(2.8284271247461903, line_length(point_1, point_2))

    def test_point4(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(5, 1)
        self.assertEqual(2.8284271247461903, line_length(point_1, point_2))

    def test_point5(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(3, 5)
        self.assertEqual(2.0, line_length(point_1, point_2))

    def test_point6(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(3, 1)
        self.assertEqual(2.0, line_length(point_1, point_2))

    def test_point7(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(1, 3)
        self.assertEqual(2.0, line_length(point_1, point_2))

    def test_point8(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(5, 3)
        self.assertEqual(2.0, line_length(point_1, point_2))

    def test_point9(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(-3, 3)
        self.assertEqual(6.0, line_length(point_1, point_2))

    def test_point10(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(-3, -3)
        self.assertEqual(8.48528137423857, line_length(point_1, point_2))

    def test_point11(self):
        point_1 = Coordinates(3, 3)
        point_2 = Coordinates(3, -3)
        self.assertEqual(6.0, line_length(point_1, point_2))

    def test_point12(self):
        point_1 = Coordinates(-3, 3)
        point_2 = Coordinates(0, 0)
        self.assertEqual(4.242640687119285, line_length(point_1, point_2))

    def test_point13(self):
        point_1 = Coordinates(1, 2)
        point_2 = Coordinates(0, 2)
        self.assertEqual(1.0, line_length(point_1, point_2))

    def test_point14(self):
        point_1 = Coordinates(1, 2)
        point_2 = Coordinates(-1, -5)
        self.assertEqual(7.280109889280518, line_length(point_1, point_2))

    def test_point15(self):
        point_1 = Coordinates(1, 2)
        point_2 = Coordinates(2, -2)
        self.assertEqual(4.123105625617661, line_length(point_1, point_2))

