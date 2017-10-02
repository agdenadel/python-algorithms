import unittest
from knn import KNN
from ...utilities.distance_functions import euclidean_distance
from point import EuclideanPoint


class DistanceFunctionTests(unittest.TestCase):
    def test_knn(self):
        knn = KNN(2, euclidean_distance)
        points = []
        for i in range(10):
            for j in range(10):
                if i > 5:
                    points.append(EuclideanPoint((i, j), 'red'))
                else:
                    points.append(EuclideanPoint((i, j), 'blue'))

        self.assertEqual(knn.predict(EuclideanPoint((0, 0), None), points), 'blue')


if __name__ == '__main__':
    unittest.main()
