"""
题目描述
一只青蛙一次可以跳上1级台阶，
也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
"""

"""
分析：
逆推：
ttj(n) = ttj(n-1) + ttj(n-2) + ... + ttj(1)；
再递推得到ttj(n) = 2 * ttj(n-1)；
递归
"""
#coding:utf-8
def ttj(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return 2 * ttj(n-1)

