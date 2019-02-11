'''
二进制中1的个数
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
'''
分析：

'''
class Solution:
    def NumberOf1(self, n):
        num = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            num += 1
            n = (n-1)&n
        return num

    def NumberOf2(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.num('1')
    def PowerOf2(self, n):
        if n&(n-1) == 0:
            return True
        else:
            return False
   
    def AndOr(self, m, n):
        diff = m^n
        num = 0
        while diff:
            num += 1
            diff = diff&(diff-1)
        return num