'''
按之字形顺序打印二叉树
请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''
'''
分析：

用两个栈实现。
python则偶数行逆序reverse()
本题要求之字打印，即奇数行左序，偶数行右序


'''
class Solution():
    def zigzag(self, pRoot):
        if not pRoot:
            return None
        else:
            layer = [pRoot]
            results = []
            nextlayer = []
            time = 1
            for node in layer:
                results.append(node.val)
                if node.left:
                    nextlayer.append(node.left)
                if node.right:
                    nextlayer.append(node.right)
                if time % 2 == 0:
                    results.reverse()
        return results





