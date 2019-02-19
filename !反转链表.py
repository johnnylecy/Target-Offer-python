'''
反转链表
输入一个链表，反转链表后，输出新链表的表头。
'''
'''
三指针方法，空间O（1）,新建三个结点pNode, pNext, pPrev
'''
class Solution():
    def ReverseList(self, pHead):
        reverseHead = None
        pNode = pHead
        pPrev = None
        if not pHead:
            pNext = pNode.next
            if not pHead.next:
                reverseHead = pHead
            else:
                pNode.next = pPrev
                pPrev = pNode
                pNext = pNode
        return reverseHead
'''
方法2：递归
'''
class Solution():
    def ReverseList(self, pHead):
        if not pHead or not pHead.next:
            return pHead

        else:
            reverseHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None

    return reverseHead
    







