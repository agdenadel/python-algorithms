from collections import Counter


class KNN():
    """ Implements K Nearest Neighbors classifier. """

    def __init__(self, k, distance_function):
        """
        
        Args:
        k (int): The number of neighbors used for voting
        distance_function (function(point, point)): A function used to compute the distance between two points
        
        """
        self.k = k
        self.distance_function = distance_function

    @staticmethod
    def vote(nearest_neighbors):
        """ Returns the most common label among the k nearest neighbors

        Args:
            nearest_neighbors (iterable): The k nearest neighbors
        """
        labels = Counter(map(lambda x: x.label, nearest_neighbors))
        winning_label = max(labels, key=labels.get)

        return winning_label

    def predict(self, test_value, training_set):
        """
        Predicts label for a point using the k nearest neighbors algorithm.

        Args:
            test_value:
            training_set:
        """       
        nearest_neighbors = sorted(training_set, key=lambda x: self.distance_function(test_value.coordinate, x.coordinate))[0:self.k]
        return self.vote(nearest_neighbors)

    def predict_multiple(self, test_values, training_set):
        """
        Predicts labels for multiple points using the k nearest neighbors algorithm.

        Args:
            test_values (iterable): 
            training_set (iterable):
        """
        return map(lambda test_value: self.predict(test_value, training_set), test_values)