class sortingAlgorithms:
        # BUBBLE_SORT
        def bubbleSort(array):
            swapped = False
            for i in range(len(array) - 1, 0, -1):
                for j in range(i):
                    if array[j] > array[j + 1]:
                        array[j], array[j + 1] = array[j + 1], array[j]
                        swapped = True
                if swapped:
                    swapped = False
                else:
                    break
            return array

        # INSERTION_SORT
        def insertionSort(array):
            for i in range(1, len(array)):
                key = array[i]
                j = i - 1
                while array[j] > key and j >= 0:
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = key
            return array

        # SELECTION_SORT
        def selectionSort(array):
            for i in range(len(array) - 1):
                min_idx = i
                for idx in range(i + 1, len(array) - 1):
                    if array[idx] < array[min_idx]:
                        min_idx = idx
                array[i], array[min_idx] = array[min_idx], array[i]
            return array

        # HEAP_SORT

        def heapify(array, n, i):
            largest = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and array[i] < array[l]:
                largest = l

            if r < n and array[largest] < array[r]:
                largest = r

            if largest != i:
                array[i], array[largest] = array[largest], array[i]
                heapify(array, n, largest)

        def heapSort(array):
            n = len(array)
            for i in range(n // 2, -1, -1):
                heapify(array, n, i)
            for i in range(n - 1, 0, -1):
                array[i], array[0] = array[0], array[i]
                heapify(array, i, 0)
            return array

        # MERGE_SORT
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            mid = (len(nums) - 1) // 2
            lst1 = mergeSort(nums[:mid + 1])
            lst2 = mergeSort(nums[mid + 1:])
            result = merge(lst1, lst2)
            return result

        def merge(lst1, lst2):
            lst = []
            i = 0
            j = 0
            while (i <= len(lst1) - 1 and j <= len(lst2) - 1):
                if lst1[i] < lst2[j]:
                    lst.append(lst1[i])
                    i += 1
                else:
                    lst.append(lst2[j])
                    j += 1
            if i > len(lst1) - 1:
                while (j <= len(lst2) - 1):
                    lst.append(lst2[j])
                    j += 1
            else:
                while (i <= len(lst1) - 1):
                    lst.append(lst1[i])
                    i += 1
            return lst

            # QUICK_SORT

        def quickSort(array):
            if len(array) > 1:
                pivot = array.pop()
                grtr_lst, equal_lst, smlr_lst = [], [pivot], []
                for item in array:
                    if item == pivot:
                        equal_lst.append(item)
                    elif item > pivot:
                        grtr_lst.append(item)
                    else:
                        smlr_lst.append(item)
                return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
            else:
                return array

        # SHELL_SORT
        def shellSort(array):
            n = len(array)
            interval = n // 2
            while interval > 0:
                for i in range(interval, n):
                    temp = array[i]
                    j = i
                    while j >= interval and array[j - interval] > temp:
                        array[j] = array[j - interval]
                        j -= interval

                    array[j] = temp
                interval //= 2
            return array

nums = [3,7,5,6,1,8,9]

print(sortingAlgorithms.heapSort(nums))