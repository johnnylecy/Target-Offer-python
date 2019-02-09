'''
按之字形顺序打印二叉树
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''
分析：
按层打印树属于BFS，用队列解决；
本题要求之字打印，即奇数行左序，偶数行右序
(未完待续)

'''
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution():
    def zprint(self, node):
        queue = []
        layer = 0
        if not node:
            print(queue)
        elif node.left or node.right:
            self.leftrecur(node, queue)
            if layer % 2 != 0:
                self.leftrecur(node, queue)
            elif layer % 2 == 0:
                self.rightrecur(node, queue)
            

    def leftrecur(self, node, queue):
        tree_list = []
        if node:
            queue.append(node)
            temp = node
            if temp.left:
                queue.append(node.left, queue)
            if temp.right:
                queue.append(node.right, queue)
            tree_list.append(queue)


    def rightrecur(self, node, queue):
        if node:
            queue.append(node)
            
            if queue[0].right:
                queue.append(node.right, queue)
            if queue[0].left:
                queue.append(node.left, queue)
            print(queue[0].val)
            queue.pop(0)
            self.leftrecur(queue[0], queue)









