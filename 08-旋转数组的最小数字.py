#coding:utf-8
import numpy as np

"""
题目描述
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""

"""

非减数组，二分查找，利用旋转,复杂度O(logn)

"""
def solution(arr):
    h = arr.size
    if h == 0:
        return 0
    start = 0
    end = h -1 
    mid = (start + end) // 2
    while not (arr[mid]<= arr[start] and arr[mid]>= arr[end]):
        if arr[mid] >= arr[start]:
            end = mid
        elif arr[mid] < arr[start]:
            start = mid
        mid = (start + end) // 2
    return arr[mid]



if __name__ == '__main__':
    s = solution(np.array([4, 6, 12, 13, 26, 1, 2, 3, 4]))
    print(s)