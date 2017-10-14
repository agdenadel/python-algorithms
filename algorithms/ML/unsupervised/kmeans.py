from ...utilities.point import average_point
from random import sample

class KMeans:
    """ Implements K-means clustering. """

    def __init__(self, k, max_iterations, distance_function):
        """

        Args:
        k (int): The number of clusters
        max_iterations (int):
        distance_function (function(point, point)): A function used to compute the distance between two points

        """
        self.k = k
        self.max_iterations = max_iterations
        self.distance_function = distance_function

    def get_random_centroids(self, points):
        # use random points as centroids
        return sample(points, self.k)

    def create_clusters(self, centroids, data):
        clusters = [[] for i in range(self.k)]
        for i in range(len(data)):
            point = data[i]
            closest_centroid_index = self.get_closest_centroid(point, centroids)
            clusters[closest_centroid_index].append(i)
        return clusters

    @staticmethod
    def get_centroids(clusters, data):
        centroids = []
        for cluster in clusters:
            points_in_cluster = []
            for i in cluster:
                points_in_cluster.append(data[i])
            centroids.append(average_point(points_in_cluster))
        return centroids

    def get_closest_centroid(self, point, centroids):
        closest_index = None
        closest_distance = float('inf')
        for i in range(len(centroids)):
            centroid = centroids[i]
            current_distance = self.distance_function(point.coordinate, centroid.coordinate)
            if current_distance < closest_distance:
                closest_index = i
                closest_distance = current_distance
        return closest_index

    def predict(self, data):
        centroids = self.get_random_centroids(data)
        for i in range(self.max_iterations):
            clusters = self.create_clusters(centroids, data)
            last_centroids = centroids
            centroids = self.get_centroids(clusters, data)

        closest_centroids = map(lambda x: self.get_closest_centroid(x, centroids), data)

        return closest_centroids, centroids
