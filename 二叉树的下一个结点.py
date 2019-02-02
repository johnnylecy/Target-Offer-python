'''
题目描述
给定一个二叉树和其中的一个结点，
请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
'''
分析：
中序遍历，left-root-right；
分情况讨论：节点有右孩子，则下一节点为右孩子最左叶子,如果其右孩子无左孩子，则为右孩子
节点没有右孩子，下一节点为father,特殊情况是该节点为其父节点右孩子，且无右子孩子

'''

class TreeNode():
    def __init__(self, x):
        self.node = x
        self.left = None
        self.right = None
        self.father = None
class Slt():
    def method(self, node):
        if node == None:
            return None
        tnext = None
        if node.right != None:
            tnext = node.right
            while tnext.left != None:
                tnext = tnext.left
        
        elif node.father.right == node:
            tnext = node
        else:
            tnext = node.father            
            
        return tnext

