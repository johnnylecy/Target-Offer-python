#coding:utf-8
import numpy as np
"""
题目描述
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中任意一个重复的数字。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
"""

"""
前提条件是一个长度为n的数组里的所有数字都在0到n-1的范围内，所以利用好下标。
"""
def solution(arr):
    idx_list = list(np.zeros_like(arr))
    for i, e in enumerate(arr):
        idx_list[arr[i]] += 1
        if idx_list[arr[i]] > 1:
            return arr[i]




if __name__ == '__main__':
    s = solution(np.array([1,0,2, 3, 4, 5, 6, 7, 0, 7, 8, 9]))
    print(s)