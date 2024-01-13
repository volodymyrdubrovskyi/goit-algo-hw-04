import timeit, random


def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos-1] > cursor:
            arr[pos] = arr[pos-1]
            pos = pos - 1
        arr[pos] = cursor    
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1
    return merged

if __name__ == '__main__':
    data_small = [random.randint(0,10000) for _ in range(1000)]
    data_medium = [random.randint(0,10000) for _ in range(10000)]

    time1_insertion = timeit.timeit(lambda: insertion_sort(data_small[:]), number=10)
    time1_merge = timeit.timeit(lambda: merge_sort(data_small[:]), number=10)
    time1_timsort = timeit.timeit(lambda: data_small[:].sort(), number=10)

    time2_insertion = timeit.timeit(lambda: insertion_sort(data_medium[:]), number=10)
    time2_merge = timeit.timeit(lambda: merge_sort(data_medium[:]), number=10)
    time2_timsort = timeit.timeit(lambda: data_medium[:].sort(), number=10)

    print(f"{'Sort method':<20} | {'Small dataset':<20} | {'Medium dataset'}")
    print(f"{'-'*63}")
    print(f"{'Insertion sort': <20} | {time1_insertion:<20.5f} | {time2_insertion:<20.5f}")
    print(f"{'Merge sort': <20} | {time1_merge:<20.5f} | {time2_merge:<20.5f}")
    print(f"{'Timsort': <20} | {time1_timsort:<20.5f} | {time2_timsort:<20.5f}")