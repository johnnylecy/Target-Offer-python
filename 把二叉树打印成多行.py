'''
把二叉树打印成多行:
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''
'''
分析：
计算节点深度，相同深度节点汇集, O(logn)
'''
class TreeNode():
    def __init__(self, x):
        self.x = x
        self.left = None
        self.right = None
        self.depth = None
def getdepth(node):
    depth = 0
    while not node:
        depth += 1
        getdepth(node.left)
        getdepth(node.right)
    return depth
def up2downprint(node):
    depth = getdepth(node)
    for i in range(depth):
        up2down_list = [node.x if node.depth==i]
        print(up2down_list)



        





        




