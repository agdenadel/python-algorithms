import unittest
from knn import KNN
from ...utilities.distance_functions import euclidean_distance
from ...utilities.point import Point


class KNNTests(unittest.TestCase):
    def test_knn(self):
        knn = KNN(2, euclidean_distance)
        points = []
        for i in range(10):
            for j in range(10):
                if i > 5:
                    points.append(Point((i, j), 'red'))
                else:
                    points.append(Point((i, j), 'blue'))

        self.assertEqual(knn.predict(Point((0, 0), None), points), 'blue')


if __name__ == '__main__':
    unittest.main()
