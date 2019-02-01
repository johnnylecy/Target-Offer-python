"""
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""
"""
分析：
跳台阶；横着2步， 竖着1步
"""
#coding:utf-8
def jzfg(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n > 1:
        return jzfg(n-1) + jzfg(n-2)