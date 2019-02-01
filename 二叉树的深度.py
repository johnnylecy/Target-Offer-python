"""
题目描述
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度
"""
"""
分析：
深度优先搜索DFS，递归
"""
class TreeNode():
    def __init__(self, x=None):
        self.x = x
        self.left = None
        self.right = None

class Slt():
    def method(self, root):
        if root == None:
            return 0
        else:
            return max(self.method(root.left), self.method(root.right) + 1

