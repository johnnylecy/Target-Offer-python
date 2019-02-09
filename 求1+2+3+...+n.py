'''
求1+2+3+...+n
求1+2+3+...+n，
要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
'''
'''
分析:
1）sum()，range()函数
2）逆推递归，递归终结条件用逻辑运算确定;
逻辑与的短路特性代替if语句
'''
class SumN():
    def __init__(self):
        self.result = 0
    def sumN(self, n):
        self.recurs(n)
        return self.result
    def recurs(self, n):
        self.result += n
        n -= 1
        return n > 0 and self.sumN(n)



