'''
题目描述
输入两个链表，找出它们的第一个公共结点。
'''
'''
分析：
遍历一个链表，装入hash表，遍历另一个链表直到有公共节点
'''
class LlistNode():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Solution():
    def FindFirstCommonNode(self, pHead1, pHead2):
        hash = dict()
        while pHead1:
            hash[pHead1] = pHead1.val
            pHead1 = pHead1.next
        while pHead2:
            if pHead2 in hash:
                return pHead2
            else:
                pHead2 = pHead2.next
        return None



