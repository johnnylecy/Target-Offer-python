'''
题目：
操作给定的二叉树，将其变换为源二叉树的镜像。
'''
#coding:utf-8
"""
分析：
递归，每一个子树的left和right互换。
"""
class Node():
    def __init__(self, x=None):
        self.x = x
        self.left = None
        self.right = None

class Slt():
    def method(self, root):
        temp = root.left
        root.left = root.right
        root.right = temp
        self.method(root.left)
        self.method(root.right)



