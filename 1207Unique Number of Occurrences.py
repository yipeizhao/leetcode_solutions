#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 11:34:22 2024

@author: yipei
"""
def Solution(arr):
    arr_set = set(arr)
    res = []
    for item in arr_set:
        res.append(arr.count(item))
    return True if len(res)-len(set(res))==0 else False
arr = [1,2]
print(Solution(arr))