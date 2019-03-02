'''
反转链表
输入一个链表，反转链表后，输出新链表的表头。
'''
'''
三指针方法，空间O（1）,新建三个结点pNode, pNext, pPrev
'''
class Solution():
    def ReverseList(self, pHead):
        if pHead == None or pHead.next == None:
           return pHead
        pre = None
        cur =pHead
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    




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
    







