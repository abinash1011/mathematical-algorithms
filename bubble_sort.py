import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr



arr1 = [12, 43, 24, 45, 33]

time_start = time.time()
sorted_array = bubble_sort(arr1)
time_end = time.time()

print(sorted_array)
print((time_end - time_start)*1000)