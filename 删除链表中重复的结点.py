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
class Solution():
    def deleteDuplication(self, pHead):
        if pHead == None: return
        prenode = None
        curnode = pHead
        nextnode = curnode.next
        if nextnode != None:
            if curnode == nextnode:
                nextnode = nextnode.next
                curnode.next = nextnode
            else:
                curnode = nextnode
                nextnode = nextnode.next
                

