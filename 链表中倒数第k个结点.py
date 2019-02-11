'''
链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。
'''
class Solution:
    def FindKthToTail(self, head, k):
        if head == None or k <= 0:
            return None

        pAHead = head
        pBehind = None

        for i in range(k-1):
            if pAHead.next != None:
                pAHead = pAHead.next
            else:
                return None
        pBehind = head
        while pAHead.next != None:
            pAHead = pAHead.next
            pBehind = pBehind.next
        return pBehind