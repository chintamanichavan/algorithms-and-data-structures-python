def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_select(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)

        if pivot_index == k:
            return arr[pivot_index]

        if pivot_index < k:
            return quick_select(arr, pivot_index + 1, high, k)
        else:
            return quick_select(arr, low, pivot_index - 1, k)


def kth_smallest(arr, k):
    if k > 0 and k <= len(arr):
        return quick_select(arr, 0, len(arr) - 1, k - 1)
    return None


# Example usage
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
k = 5
result = kth_smallest(arr, k)
print(f"The {k}-th smallest element is {result}")
