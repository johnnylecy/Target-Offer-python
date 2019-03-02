#coding:utf-8
import numpy as np
"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
重复的结点不保留，返回链表头指针。 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""
"""
分析:排序链表，重复节点在一起，判断node.data和node.next是否相等，
继续next所得node.data如果相等则继续next，否则delete.用C语言来做就是熟悉的“三指针”套路。
"""
class ListNode():
def __init__(self, x):
    self.val = x
    self.next = None

class Solution():
    def deleteDuplication(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        prenode = ListNode(0)
        prenode.next = pHead
        curnode = pHead
        nextnode = pHead.next
        
        while nextnode:
            dele = False
            while curnode.val == nextnode.val:
                dele = True
                curnode = nextnode
                nextnode = nextnode.next
            if dele:
                prenode.next = nextnode
            elif nextnode.next:
                curnode = nextnode
                nextnode = nextnode.next

