#coding:utf-8
'''
归并排序仍然是利用完全二叉树实现
'''
class Merge():
    def merge_sort(self, data):
        if len(data) <= 1:
            return data
        
        mid = len(data) // 2
        left = self.merge_sort(data[:mid])
        right = self.merge_sort(data[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        # double points
        i = j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result
data = [100,11,8,9,6,2,4,5,7,1,10,3]
M = Merge()
print(M.merge_sort(data))

