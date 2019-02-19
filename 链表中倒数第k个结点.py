'''
链表中倒数第k个结点
输入一个链表，输出该链表中倒数第k个结点。
'''
'''
思路是设置两个指针，第一个指针先走k-1结点，然后一起走，直到第一个结点next为None
'''
class Solution():
    def FindKth2Tail(self, pHead, k):
        pNode_1 = pHead
        pNode_2 = pHead
        if not pHead or k <= 0:
            return None
        else:
            for i in range(k-1):
                if pNode_1.next:
                    pNode_1 = pNode_1.next
                else:
                    return None

            if pNode_1.next:
                pNode_2 = pNode_2.next
            else:
                return pNode_2