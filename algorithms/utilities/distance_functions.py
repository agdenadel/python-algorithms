import math

def euclidean_distance(x, y):
    return math.sqrt(sum(map(lambda x: (x[0] - x[1]) ** 2, zip(x,y))))