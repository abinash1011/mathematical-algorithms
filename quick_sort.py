import time

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot-1)
        quick_sort(arr, pivot+1, high)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1



arr1 = [12, 43, 24, 45, 33]

time_start = time.time()
sorted_array = quick_sort(arr1, 0, 4)
time_end = time.time()

print(sorted_array)
print((time_end - time_start)*1000)