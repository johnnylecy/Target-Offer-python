#coding:utf-8
import numpy as np

"""
题目描述:
    在一个二维数组中（每个一维数组的长度相同），
    每一行都按照从左到右递增的顺序排序，
    每一列都按照从上到下递增的顺序排序。
    请完成一个函数，
    输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""

"""

有序数组，从左下角开始查找，复杂度为O(m + n),比二分查找O(mlogn)要好一些

"""
def find(arr, target):
    arr = np.asarray(arr)
    (h, w) = arr.shape
    start = [h-1, 0]
    while start[0] > 0 and start[1] < w:
        if arr[start[0], start[1]] < target:
            start[1] += 1            
        elif arr[start[0], start[1]] > target:
            start[0] -= 1
        else: return True
    return False
if __name__ == '__main__':
    find(np.ones((3000, 10000)), 2)

    


    

