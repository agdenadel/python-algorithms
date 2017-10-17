from euclidean_algorithm import euclidean_algorithm


def least_common_multiple(x, y):
    return x * y / euclidean_algorithm(x, y)