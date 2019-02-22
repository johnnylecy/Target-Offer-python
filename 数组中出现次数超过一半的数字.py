'''
题目描述
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''
'''
哈希表O（N）:边计数边判断，但判断哈希值是否存在有作弊嫌疑；
利用数组特性
python collections import Counter
'''
class Solution:
    def MoreThanHalfNum_Solution(self, arr):
        Hash = dict()
        for a in arr:
            if a not in Hash:
                Hash[a] = 1
            else:
                Hash[a] += 1
            if Hash[a] > len(arr) / 2:
                return a
        return 0
    def py_solution(self, arr):
        tmp = collections.Counter(arr) # 返回一个计数字典
            x = len(arr) / 2
            for k, v in tmp.items():
                if v > x:
                    return k
            return 0
