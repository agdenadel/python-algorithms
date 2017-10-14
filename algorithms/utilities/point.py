from __future__ import division


class Point:
    def __init__(self, coordinate, label):
        self.coordinate = coordinate
        self.label = label

    def __str__(self):
        return "Point: {" + "coordinate: " + str(self.coordinate) + ", label: " + str(self.label) + "}"


def average_point(points):
    sums = [0] * len(points[0].coordinate)  # initialize with dimension of each point
    for point in points:
        for i in range(len(point.coordinate)):
            sums[i] += point.coordinate[i]

    return Point(tuple(map(lambda x: x / len(points), sums)), None)
