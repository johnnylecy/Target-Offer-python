'''
复杂链表的复制
输入一个复杂链表（
每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（
注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
'''
class Solution():

'''
方法1:散列，先复制节点和next指针，然后用散列将结点一一对应起来。
然后复制random指针。在散列中旧链表N节点random指针指向S，则对应节点N' random指向S’
'''
    def copyList(self, pHead):
        if not pHead:
            return None
            
        else:
            Hash = dict()
            pNode = pHead
            while pNode.next:
                
                Hash[pNode] = RandomList(0)
                Hash[pNode].x = pNode.x
                Hash[pNode].next = pNode.next
                Hash[pNode].random = pNode.random
                pNode = pNode.next
        return Hash[pHead]
'''
方法2:
空间O(1)
新结点N’copy之后 N.next=N',相应的N.random.next = N'.random
然后形成一个zigzag走位链表，偶数位置结点取出并next指针相连就是copypList
'''
    def copyList(self, pHead)；
        if not pHead:
            return None
        else:
            
            pNode = pHead
            daulpHead = pNode
           
            while pNode.next:
                copypNode = RandomList(0)
                copypNode.x = pNode.x
                copypNode.next = pNode.next
                # copypNode.random = pNode.random
                
                pNode.next = copypNode               
                # pNode.random.next = copypNode.random
                # if pNode.random:
                #     copypNode.random = pNode.random
                #     pNode.random.next = copypNode.random
                pNode = copypNode.next
            # if daulpHead.random:

            #reconnect
            pNode1 = daulpHead
            pNode2 = daulpHead.next
            copypHead = pNode2
            while pNode1.next.next:
                pNode2.next= pNode1.next.next.next
                if pNode1.random:
                    pNode2.random = pNode1.random.next
                pNode1 = pNode1.next.next
                pNode2 = pNode2.next.next
        return copyHead







            