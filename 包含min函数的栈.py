'''
包含min函数的栈
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
'''
'''
缓存Min,入栈和出栈都要来考虑
'''
class Solution():
    def __init__(self):
        self._elems = [] # list对象 存储栈中元素，将栈操作映射到list操作
        self.temp = None

    def push(self, elem):
        if not self.temp:
            self.temp = elem
            self._elems.append(elem)
        if self.temp <= elem:
            self._elems.append(elem)
        if self.temp > elem:
            self.temp = elem

    def pop(self):
        if not self.temp: 
            self.temp = self.top()
        if self.temp <= self.top()
            pass
        if self.temp > self.top():
            self.temp = self.top()
        return self._elems.pop()

    def top(self):
        if self._elems == []:
            pass
        return self._elems[-1]
    def min(self):
        return self.temp
        


