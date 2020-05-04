"""
Created on Tue May 5 02:11:39 2020

@author: Danilov Evgeniy
"""

def quick_sort_recursion(arr: list):
    """QuickSort с помощью применения рекурсии"""
    if len(arr) < 2:
        return arr
    else:
        # Выбираем опорную точку. Оптимальный выбор взять случайный элемент массива
        pivot = arr[0]
        less    = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]

        return quick_sort_recursion(less) + [pivot] + quick_sort_recursion(greater)

# Проверим результат работы алгоритма
print(quick_sort_recursion([1, 4, 2, 44, 3, 12,99, 7]))
print(quick_sort_recursion([11,-4,0,44,31, 122, 99, -7]))