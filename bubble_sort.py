"""
Created on Sat May 3 19:57:39 2020

@author: Danilov Evgeniy
"""

# Bubble sort
def bubble_sort(ansort: list):       
    i = 0
    m = 0
    while i < len(ansort):
        for x in range(len(ansort)-1):
            if ansort[x] > ansort[x+1]:
                ansort[x], ansort[x+1] = ansort[x+1], ansort[x]
            m += 1
        i += 1
    sort = ansort
    return sort

# Test some lists
assert(bubble_sort([2, 1, 6, 3])) == [1, 2, 3, 6]
assert(bubble_sort([99, 2, 1, 88, 33])) == [1, 2, 33, 88, 99]
assert(bubble_sort([2, 3, 1])) == [1, 2, 3]