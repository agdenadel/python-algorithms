import unittest
from kmeans import KMeans
from ...utilities.distance_functions import euclidean_distance
from ...utilities.point import Point


class KMeansTests(unittest.TestCase):
    def test_knn(self):
        kmeans = KMeans(2, 500, euclidean_distance)
        points = []
        for i in range(10):
            for j in range(10):
                if i < 3 and j < 3:  # first cluster near origin
                    points.append(Point((i, j), None))
                elif i > 6 and j > 6:  # second cluster near (10, 10)
                    points.append(Point((i, j), None))

        closest_centroids, centroids = kmeans.predict(points)

        # first cluster
        self.assertEqual(closest_centroids[0], closest_centroids[1])
        self.assertEqual(closest_centroids[0], closest_centroids[2])
        self.assertEqual(closest_centroids[0], closest_centroids[3])
        self.assertEqual(closest_centroids[0], closest_centroids[4])
        self.assertEqual(closest_centroids[0], closest_centroids[5])
        self.assertEqual(closest_centroids[0], closest_centroids[6])
        self.assertEqual(closest_centroids[0], closest_centroids[7])
        self.assertEqual(closest_centroids[0], closest_centroids[8])
        # second cluster
        self.assertEqual(closest_centroids[9], closest_centroids[10])
        self.assertEqual(closest_centroids[9], closest_centroids[11])
        self.assertEqual(closest_centroids[9], closest_centroids[12])
        self.assertEqual(closest_centroids[9], closest_centroids[13])
        self.assertEqual(closest_centroids[9], closest_centroids[14])
        self.assertEqual(closest_centroids[9], closest_centroids[15])
        self.assertEqual(closest_centroids[9], closest_centroids[16])
        self.assertEqual(closest_centroids[9], closest_centroids[17])

unittest.main()
