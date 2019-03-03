'''
题目描述
输入一颗二叉树的跟节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
'''
分析：
先序遍历，难点在于检查完左子树之后，如何将路径恢复到之前状态检查右子树。
解决方法是递归
典型递归实现， 与数学归纳法反方向。
需要找出满足条件的路径，路径一定要到最后的节点
递归顺序满足回溯
'''
class Solution():
    def FindPath(self, root, expectNumber):
        self.paths = []
        self.expectNumber = expectNumber
        if root == None:
            pass 
        else:
            self.DFS(root, [root.val])
        return self.paths

    def DFS(self, root, path):
        if not root.left and not root.right and sum(path) == self.expectNumber:
            self.paths.append(path)
        if root.left and sum(path) < self.expectNumber:
            self.DFS(root.left, path + [root.left.val])
        if root.right and sum(path) < self.expectNumber:
            self.DFS(root.right, path + [root.right.val])
            



        