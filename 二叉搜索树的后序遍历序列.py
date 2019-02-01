"""
题目描述
输入一个整数数组，
判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
#coding:utf-8
"""
分析：
BTS性质；递归
"""
class Slt():
    def right(self, a):
        i = 0
        while i < len(a):
            if a[i] >= a[-1]:
                i += 1
            else:
                print('No')
                continue
    def method(self, a):
        i = 0
        while i < len(a):
            if a[i] <= a[-1]:
                i += 1
            elif i = 0:
                print('No')
            else:
                self.method(a[:i])
                self.right(a[i: len(a)])
        print('Yes')
            