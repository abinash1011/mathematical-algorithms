import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


arr1 = [12, 43, 24, 45, 33]

time_start = time.time()
sorted_array = insertion_sort(arr1)
time_end = time.time()

print(sorted_array)
print((time_end - time_start)*1000)