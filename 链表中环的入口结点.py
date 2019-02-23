'''
题目描述
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。
'''
'''
分析：
时间复杂度O(n).
空间复杂度O(1)，不可以使用hash
'''
class Solution():
    def MeetingNode(self, pHead):
        if not pHead:
            return None

        pSlow = pHead
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next
    
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None

        NodeLoop = 1
        flagNode = meetingNode
        while flagNode.next != meetingNode:
            NodeLoop += 1
            flagNode = flagNode.next

        pFast = pHead
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast


        
