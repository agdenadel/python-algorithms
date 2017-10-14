def bubble_sort(array):
    swapped = True
    array = list(array) # work on copy of original list
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                tmp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = tmp
                swapped = True
    return array
