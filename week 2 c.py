# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:12:48 2019

@author: sri
"""

def listcheck(Count, N):
    li = []
    for i in range(Count):
        n = int(input('Enter element for list : '))
        li.append(n)
        li.sort()
    print(li)
    if N in li:
        return True
    else:
        return False

Count = int(input('Enter the no of elements that you want to add into the list : '))
N = int(input('Enter a number that you want to search in the list : '))
output = listcheck(Count, N)
print(output)  