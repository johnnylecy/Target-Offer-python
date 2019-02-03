'''
题目描述
请实现一个函数，
用来判断一颗二叉树是不是对称的。
注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
'''
'''
分析：
递归判断每一个节点左右孩子是否相等
'''

def ismirror(node):
    while node:
        if node.left != node.right:
            return False
        else:
            ismirror(node.left)
            ismirror(node.right)
    return True
            
            
            

    

