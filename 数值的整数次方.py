'''
题目描述
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
'''
'''
分析：

'''
class Solution:
    def method(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        if exponent == -1:
            return 1/base

        result = self.method(base, exponent >> 1)
        result *= result
        if (exponent & 0x1) == 1:
            result *= base
        return result