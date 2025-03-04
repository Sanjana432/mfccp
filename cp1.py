import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Function to compare the performance of sorting algorithms
def compare_sorting_algorithms():
    arr = [random.randint(0, 10000) for _ in range(1000)]  # Generate a list of random numbers

    # Bubble Sort
    start_time = time.time()
    bubble_sort(arr.copy())  # Using copy to prevent sorting the same list multiple times
    bubble_sort_time = time.time() - start_time
    print(f"Bubble Sort Time: {bubble_sort_time:.6f} seconds")

    # Selection Sort
    start_time = time.time()
    selection_sort(arr.copy())
    selection_sort_time = time.time() - start_time
    print(f"Selection Sort Time: {selection_sort_time:.6f} seconds")

    # Insertion Sort
    start_time = time.time()
    insertion_sort(arr.copy())
    insertion_sort_time = time.time() - start_time
    print(f"Insertion Sort Time: {insertion_sort_time:.6f} seconds")

# Call the function to compare sorting algorithms
compare_sorting_algorithms()
