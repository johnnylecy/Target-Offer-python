'''
题目描述
在数组中的两个数字，
如果前面一个数字大于后面的数字，
则这两个数字组成一个逆序对。输入一个数组,
求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
输入描述:
题目保证输入的数组中没有的相同的数字

数据范围：

	对于%50的数据,size<=10^4

	对于%75的数据,size<=10^5

	对于%100的数据,size<=2*10^5
'''
'''
分析：归并排序O(nlogn)
树形数组
'''
class Solution():
	#Merge-sort
	def inverse_pairs(self, data):
		p = 0
		if len(data) <= 1:
			return data, p
		mid = len(data) // 2
		left, p = self.inverse_pairs(data[:mid])
		right, p = self.inverse_pairs(data[mid:])
		return self.merge(left, right, p)

	def merge(self, left, right, p):
		i = j = 0
		result = []
		while i < len(left) and j < len(right):
			if left[i] < right[j]:
				result.append(left[i])
				i += 1
			else:
				result.append(right[j])
				j += 1
				p += 1
		result.extend(left[i:])
		result.extend(right[j:])
		return result, p

data = [100,11,8,9,6,2,4,5,7,1,10,3]
M = Solution()
print(M.inverse_pairs(data))




