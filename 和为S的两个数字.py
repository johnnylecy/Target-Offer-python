'''
和为S的两个数字
输入一个递增排序的数组和一个数字S，
在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
'''
'''
分析：
头尾指针，相隔越远乘积越小
'''
class Solution():
    def sumS(self, S, arr):
        i = 0
        j = -1
        if arr[i] + arr[j] == S:
            return (arr[i], arr[j])
        elif arr[i] + arr[j] > S:
            j -= 1
        elif arr[i] + arr[j] < S:
            i += 1
        


