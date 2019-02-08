'''
题目描述
输入一颗二叉树的跟节点和一个整数，
打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
(注意: 在返回值的list中，数组长度大的数组靠前)
'''
'''
分析：
先序遍历，难点在于检查玩左子树之后，如何将路径恢复到之前状态检查右子树。
解决方法是回溯法
'''
class Solution():
    def FindPath(self, root, sum):
        if not root:
            return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        stack = []
        leftStack = self.pathSum(root.left, sum - root.val)
        for i in leftStack:
            i.insert(0, root.val)
            stack.append(i)
        rightStack = self.pathSum(root.right, sum - root.val)
        for i in rightStack:
            i.insert(0, root.val)
            stack.append(i)
        return stack

    def pathSum(self, root, sum):
        if not root: return []
        if root.left == None and root.right == None:
            if sum == root.val:
                return [[root.val]]
            else:
                return []
        a = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        return [[root.val] + i for i in a]
