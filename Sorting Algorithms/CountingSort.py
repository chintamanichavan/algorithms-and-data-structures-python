def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_elements = max_value - min_value + 1
    count_array = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count_array[num - min_value] += 1

    for i in range(1, len(count_array)):
        count_array[i] += count_array[i - 1]

    for num in arr:
        output[count_array[num - min_value] - 1] = num
        count_array[num - min_value] -= 1

    for i in range(len(arr)):
        arr[i] = output[i]
