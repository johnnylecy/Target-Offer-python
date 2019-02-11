'''
题目描述
输入一个整数数组，
实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
class Solution:
    def reorderArray(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front = 0
        rear = len(array)-1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array
    
    def reorderArray2(self, array):
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right

    def reorderArray3(self, array):
        if len(array) < 1:
            return []
        if len(array) == 1:
            return array
        odd = []
        even = []
        for num in array:
            if num & 0x1:
                odd.append(num)
            else:
                even.append(num)
        return odd + even