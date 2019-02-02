'''
题目
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''
'''
分析：
递归判断节点平衡因子，但深度重复计算；

'''
#coding:utf-8
class TreNode():
    def __init_(self, x=None):
        self.x = x
        self.left = None
        self.right = None

class Slt():
    def depth(self, node):
        if node ==None:
            return 0
        else:
            return max(self.depth(node.left), self.depth(node.right)) + 1
    def mtd(self, node):
        if not node:
            return True
        else:
            lamd = self.depth(node.left) - self.depth(node.right)
            if abs(lamd) > 1:
                return False
            else:
                self.mtd(node.left)
                self.mtd(node.right)


