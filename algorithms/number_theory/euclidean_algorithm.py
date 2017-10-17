def euclidean_algorithm(x, y):
    while y:
        tmp = y
        y = x % y
        x = tmp
    return x