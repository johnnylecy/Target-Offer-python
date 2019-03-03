"""
广度优先遍历
"""
'''
用队列实现, 先放入根节点，出队一个节点，出队节点的左右结点依序入队，循环
'''
class Solution:                                      
    def PrintFromTopToBottom(self, root):
        res = []
        quene = []
        if root == None:
            return res
        quene.append(root)
        while len(quene):
            node = quene.pop(0)
            if node:
                res.append(node.val)
                quene.append(node.left)
                quene.append(node.right)
        return res