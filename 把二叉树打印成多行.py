'''
把二叉树打印成多行:
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
'''
分析：
双队列，先进先出 list append()
利用列表存储二叉树每一层的节点, 在读取列表中当前层节点的同时，存储下一层的节点以备用，以此类推
'''
class Solution():
    def layerorder(self, pRoot):
        if not pRoot:
            return None
        else:
            layer = [pRoot]
            memory = []
            queue = []
            while layer:
                for node in layer:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                    memory.append(queue)
                layer = queue
        return memory



        





        




