from sort_utilities import swap


def quick_sort(array):
    # lomuto scheme
    array = list(array) # copy array to work in place

    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] < pivot:
                i += 1
                swap(array, i, j)
        if array[high] < array[i + 1]:
            swap(array, i + 1, high)
        return i + 1

    def q_sort(array, low, high):
        if low < high:
            p = partition(array, low, high)
            q_sort(array, low, p - 1)
            q_sort(array, p + 1, high)

    q_sort(array, 0, len(array) - 1)
    return array