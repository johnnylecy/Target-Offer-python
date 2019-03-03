"""
题目描述
输入一个整数数组，
判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
#coding:utf-8
"""
分析：
BTS性质；递归
分治， 先判断root,然后判断left, right, 有False则跳出；顺利则进入left和right递归
"""
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        root = sequence[-1]
        index = 0
        l = len(sequence)
        for i in range(l-1):
            index = i
            if sequence[i] > root:
                break
                
        for i in range(index+1,l-1):
            if sequence[i] < root:
                return False
        left = True
        
        if index > 0:
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index < l - 1:
            right = self.VerifySquenceOfBST(sequence[index:l-1])
        return left and right
        
array = [5, 7, 6, 9, 11, 10, 8]
array2 = [4, 6, 7, 5]
array3 = [1, 2, 3, 4, 5]
S = Solution()
print(S.VerifySquenceOfBST(array))
print(S.VerifySquenceOfBST(array2))
print(S.VerifySquenceOfBST(array3))

            