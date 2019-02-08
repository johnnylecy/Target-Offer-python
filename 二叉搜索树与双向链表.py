'''
题目描述
输入一棵二叉搜索树，
将该二叉搜索树转换成一个排序的双向链表。
要求不能创建任何新的结点，只能调整树中结点指针的指向。
'''
'''
分析：
利用一个栈实现二叉树的中序遍历，题中说这是一颗二叉树，那么二叉树的中序遍历是一个有顺序的，  
那么这个时候只需要在中序遍历的时候当找到一个遍历节点的时候先将这个节点保存起来，
然后遍历下一个节点的时候将之前保存的节点的right域指向下一个结点，下一个结点的left域指向上一个结点。
这样一来就形成了一个排序的双向链表。然后将之前指向保存的指针指向当前这个结点。
'''
class Solution():
    def Convert(self, pRootOfTree):
        if pRootOfTree == None:
            return None
        if not pRootOfTree.left and not pRootOfTree.right:
            return pRootOfTree

        # 处理左子树
        self.Convert(pRootOfTree.left)
        left = pRootOfTree.left

        # 连接根与左子树最大结点
        if left:
            while left.right:
                left = left.right
            pRootOfTree.left, left.right = left, pRootOfTree

        # 处理右子树
        self.Convert(pRootOfTree.right)
        right = pRootOfTree.right

        # 连接根与右子树最小结点
        if right:
            while right.left:
                right = right.left
            pRootOfTree.right, right.left = right, pRootOfTree

        while pRootOfTree.left:
            pRootOfTree = pRootOfTree.left

        return pRootOfTree
