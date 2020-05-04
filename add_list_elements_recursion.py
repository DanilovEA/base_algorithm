"""
Created on Mon May 4 19:11:39 2020

@author: Danilov Evgeniy
"""

test_list = [1, 2, 3, 4, 7, 45, 22, 1, 24, 532, 23, 65, 23, 223, 22, 1]

def summ(arr: list):
    """Суммирование элементов массива в цикле"""
    res = 0
    for x in arr:
        res += x
    return res

print(summ(test_list))

def summ_recursion(arr: list):
    """Суммирование элементов массива с помощью рекурсии"""
    if arr == []:
        return 0
    else:
        return  arr[0] + summ_recursion(arr[1:])
    

print(summ_recursion(test_list))