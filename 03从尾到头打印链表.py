#coding:utf-8
import numpy as np

#题目描述
# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

"""
分析：
链表(linked list)是由一组被称为结点的数据元素组成的数据结构，
每个结点都包含结点本身的信息和指向下一个结点的地址。链表中最后一个节点的指针域为None值
1）首先用python定义一个linkedlist类；或者直接定义node也可以
2）使用insert将输入链表每个node依序insert到list第一个位置，反转之后再打印list
"""
class Solution(object):
    def __init__(self):
        super(Solution,self).__init__()
        self.linklist = []
    
    def method(self, head):
        while head:
            self.linklist.insert(0, head)
            head = head.next
        print(self.linklist)    

class Node():
    def __init__(self, v=None):
        self.v = v
        self.next = None
    def __repr__(self):
        #被打印的时候需要以字符串的形式输出的时候，
        # 就会找到这个方法，并将返回值打印出来
        # 类似方法：__str__()
        return str(self.v)
'''
思路2：反转链表
'''

node1 = Node(0)
node2 = Node(1)
node3 = Node(2)
node1.next = node2
node2.next = node3
S = Solution()
S.method(node1)



