def insertion_sort(bucket):
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and key < bucket[j]:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key

def bucket_sort(arr):
    num_buckets = len(arr)
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = int((num - min_value) // bucket_range)
        buckets[index].append(num)

    for i in range(num_buckets):
        insertion_sort(buckets[i])

    index = 0
    for i in range(num_buckets):
        for j in range(len(buckets[i])):
            arr[index] = buckets[i][j]
            index += 1
