import unittest
from point import Point, average_point


class KMeansTests(unittest.TestCase):
    def test_average_points(self):
        points = []
        for i in range(4):
                points.append(Point((i,i), None))

        avg_point = average_point(points)

        self.assertEqual(avg_point.coordinate[0], (0.0 + 1.0 + 2.0 + 3.0) / 4.0)
        self.assertEqual(avg_point.coordinate[1], (0.0 + 1.0 + 2.0 + 3.0) / 4.0)


if __name__ == '__main__':
    unittest.main()
