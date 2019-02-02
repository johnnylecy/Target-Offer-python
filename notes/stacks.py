'''
栈的实现
'''
#coding:utf-8
class SStack():
    def __init_(self):
        self._elems = []
    def is_empty(self):
        return self._elems == []
    def top(self):
        if self._elems == []:
            raise StackeUnderflow('in SStack.top()')
        return self._elms[-1]
    def push(self, elem):
        self._elems.append(elem)
    def pop(self):
        if self._elems == []:
            raise StackeUnderflow('in SStack.top()')
        return self._elems.pop()

class StackeUnderflow(ValueError):
    pass

