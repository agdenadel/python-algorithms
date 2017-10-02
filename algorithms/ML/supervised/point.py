from ...utilities.distance_functions import euclidean_distance


class EuclideanPoint():
    def __init__(self, coordinate, label):
        self.coordinate = coordinate
        self.label = label

    def distance(self, other):
        return euclidean_distance(self.coordinate, other.coordinate)