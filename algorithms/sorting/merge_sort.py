def merge_sort(array):
    def merge(arr1, arr2):
        i = j = 0
        merged = []
        while i < len(arr1) or j < len(arr2):
            if i == len(arr1) or j == len(arr2):
                merged.extend(arr2[j:])
                merged.extend(arr1[i:])
                break
            elif arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            elif arr1[i] > arr2[j]:
                merged.append(arr2[j])
                j += 1
        return merged

    if len(array) == 1 or len(array) == 1:
        return array

    return merge(merge_sort(array[0:len(array) // 2]), merge_sort(array[len(array) // 2:]))