# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random
size = 10
M = 0
N = 49
array = [random.uniform(M, N) for _ in range(size)]
print(array)

def merge_sort(array, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid, end)
        merge_list(array, start, mid, end)


def merge_list(array, start, mid, end):
    left = array[start:mid]
    right = array[mid:end]
    k = start
    i = 0
    j = 0
    while (start + i < mid and mid + j < end):
        if (left[i] <= right[j]):
            array[k] = left[i]
            i = i + 1
        else:
            array[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            array[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            array[k] = right[j]
            j = j + 1
            k = k + 1

array = [float(x) for x in array]
merge_sort(array, 0, len(array))
print('Отсортированный массив: ', end='')
print(array)


