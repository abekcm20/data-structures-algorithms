#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 15 18:26:18 2021

@author: abhishek
"""

class pair:
    def __init__(self):
        self.min = 0
        self.max = 0
 
def getMinMax(arr: list, n: int) -> pair:
    minmax = pair()
 
    # If there is only one element then return it as min and max both
    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
 
    # If there are more than one elements, then initialize min
    # and max
    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]
 
    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        if arr[i] < minmax.min:
            minmax.min = arr[i]
 
    return minmax
 
# Driver Code
if __name__ == "__main__":
    arr = [788, 11, 445, 1, 330, 3000]
    arr_size = len(arr)
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)
 