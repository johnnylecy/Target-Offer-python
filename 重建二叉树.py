"""
题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""
"""
分析：
前置条件为无重复。则前序遍历第一元素为root，中序遍历root前后分别是左，右子树。递归
"""
#coding:utf-8
class TreeNode():
    def __init__(self,x=None):
        super(TreeNode, self).__init__()
        self.x = x
        self.left = None
        self.right= None
class Solution():
    def method(self, pretr, int):
        tree = treeNode(pretr[0])
        intr_root_idx = intr.index(pretr[0])
        tree.left = method(pretr[1 : intr_root_idx+1], intr[:intr_root_idx])
        tree.right = method(pretr[intr_root_idx+2:], intr[:intr_root_idx])
        return tree
        

