# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        i = pHead1
        j = pHead2
        if pHead1.val <= pHead2.val:
            mHead = pHead1
            i = pHead1.next
        else:
            mHead = pHead2
            j = pHead2.next
        result = mHead
        while i or j:
            if i.val <= j.val:
                result.next = i
                result = i
                i = i.next
            else:
                result.next = j
                result = j
                j = j.next
        return mHead
S= Solution()
print()