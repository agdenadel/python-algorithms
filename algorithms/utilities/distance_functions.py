import math


def euclidean_distance(a, b):
    return math.sqrt(sum(map(lambda x: (x[0] - x[1]) ** 2, zip(a, b))))
