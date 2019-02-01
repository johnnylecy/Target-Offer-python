"""
输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
"""
"""
分析：
遍历A树， 看B树根节点是否和A的节点，左右子树相同，递归实现
"""
class TreeNode():
    def __init__(self, x=None):
        self.x = x
        self.left = None
        self.right = None

class Slt():
    def trav(self, A, B):
        if A == None:
            return True
        if B == None:
            return False
        if A.x != B.x:
                return False
        return self.trav(A.left, B) and self.trav(A.right, B)

