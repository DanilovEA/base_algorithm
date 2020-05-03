"""
Created on Sat May 3 21:11:39 2020

@author: Danilov Evgeniy
"""

# Сортировка массива методом выбора 

def smallest(u_arr: list):
    """Находим самое маленькое число в нашем списке"""
    smallest = u_arr[0]
    smallest_index = 0
    for x in range(len(u_arr)):
        if smallest > u_arr[x]:
            smallest = u_arr[x]
            smallest_index = x
    return smallest_index


def sort_select(unsort: list):
    """Создаём новый список и поочередно добавляем туда самые маленькие значение из оригинального списка. 
    Одновременно удаляя их из оригинального списка"""
    sort = []
    while unsort:
        sort.append(unsort.pop(smallest(unsort)))
    return sort

# Test some lists
assert(sort_select([2, 1, 6, 3])) == [1, 2, 3, 6]
assert(sort_select([99, 2, 1, 88, 33])) == [1, 2, 33, 88, 99]
assert(sort_select([2, 3, 1])) == [1, 2, 3]

