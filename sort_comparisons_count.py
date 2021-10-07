def selection_sort_comparisons(arr: list):
    comparisons = 0
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min]:
                min = j
        arr[min], arr[i] = arr[i], arr[min]
    return comparisons


def insertion_sort_comparisons(arr: list):
    comparisons = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j-1]:
            comparisons += 1
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        comparisons += 1
    return comparisons


def merge_sort_comparisons(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        comparisons += merge_sort_comparisons(left)
        comparisons += merge_sort_comparisons(right)

        comparisons += merge_comparisons(left, right, arr)
    return comparisons

def merge_comparisons(left, right, arr):
    comparisons = 0
    i = j = k = 0

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

    return comparisons


def shell_sort_comparisons(arr: list):
    comparisons = 0
    h = 1
    while h < len(arr)/3:
        h = 3*h + 1
    while h >= 1:
        for i in range(h, len(arr)):
            j = i
            while j >= h and arr[j] < arr[j-h]:
                comparisons += 1
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= 1
            comparisons += 1
        h //= 3
    return comparisons

