#coding:utf-8
import numpy as np
"""
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1],
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
"""

"""
不使用除法，复杂度尽可能低，复杂度上限是O（N**2），分治下标前后两个连乘
"""

def solution(A):
        n = len(A)
        B = [None]*n
        B[0] = 1
        for i in range(1, n):
            B[i] = B[i-1]*A[i-1]
        c = 1
        for i in range(n-2,-1,-1):
            c *= A[i+1]
            B[i] *= c
        return B

if __name_ =="__main__":
    pass