def selectionSort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for idx in range(i + 1, len(array) - 1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array