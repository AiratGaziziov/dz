import time
import random

array = [random.randint(1, 100) for _ in range(10000)]

# Алгоритм быстрой сортировки
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x > pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x < pivot]
    return quick_sort(left) + mid + quick_sort(right)

# Алгоритм пузырьковой сортировки по убыванию
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Создание копий массива для каждого алгоритма
array_quick = array[:]
array_bubble = array[:]

# Измерение времени для быстрой сортировки
start_time = time.time()
array_quick = quick_sort(array_quick)
quick_sort_time = time.time() - start_time

# Измерение времени для пузырьковой сортировки
start_time = time.time()
array_bubble = bubble_sort(array_bubble)
bubble_sort_time = time.time() - start_time

print(f"Время быстрой сортировки: {quick_sort_time:.2f} seconds")
print(f"Время пузырьковой сортировки: {bubble_sort_time:.2f} seconds")
