from sort_utilities import swap

def bubble_sort(array):
    swapped = True
    array = list(array) # work on copy of original list
    while swapped:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                swapped = True
    return array
