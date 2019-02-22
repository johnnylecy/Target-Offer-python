'''
题目描述
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''
'''
归并排序
'''
class Solution():
    def merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        
        mpHead = None
        while not pHead1.next and not pHead2.next:
            if pHead1.val <= pHead2.val:
                mpHead.next = self.merge(pHead1.next, pHead2)
                pNode1 = pNode1.next
            else:
                mpNode.next = pNode2
                pNode2 = pNode2.next
        mpNode.next = 
