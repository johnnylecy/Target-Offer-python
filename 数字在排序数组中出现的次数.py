'''
数字在排序数组中出现的次数
统计一个数字在排序数组中出现的次数。
'''
'''
分析：
两次二分查找,查到arr[mid] == k时候，判断前后索引值是否等于k,如果等于k，继续二分查找。
这里不再使用顺序查找原因是因为复杂度仍然会很高。
'''
class Solution():

    def find_forword(self, beg, end, arr)
        mid = (beg + end) // 2
        if arr[mid] == k:
            return arr[mid]
            if arr[mid-1] == k:
                return self.find_forword(beg, mid-1, arr[beg:mid])
            if arr[mid+1] == k:
                return self.find_forword(mid+1, end, arr[mid+1:])
        
        if arr[mid] < k:
            return self.find_forword(mid+1, end, arr[mid+1:])
        if arr[mid] > k:
            beg = mid
            return self.find_forword(beg, mid-1, arr[beg:mid])



