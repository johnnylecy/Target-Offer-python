'''
题目描述
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
'''
首先想到遍历，时间复杂度O（n）
时空平衡是可以实现的：上一个丑数判断出下一个丑数
'''
class Solution():
    def GetUglyNumber1(self, N):
        result = 1
        n = 0
        i = 1
        while n < N:
            if (i % 2 == 0 or i % 3 == 0 or i % 5 == 0) and i % 7 != 0:
                n += 1
                if n == N:
                    result = i
        return result

    def get_uglynumber(self, N):
        lst = [1] * N
        p2 = 0
        p3 = 0
        p5 = 0
        i = 1
        while i < N:
            minv = min(lst[p2]*2, lst[p3]*3, lst[p5]*5)
            lst[i] = minv
            if lst[p2]*2 == minv:
                p2 += 1
            if lst[p3]*3 == minv:
                p3 += 1
            if lst[p5]*5 == minv:
                p5 += 1
            i += 1
        return lst[-1]
S = Solution()
print(S.get_uglynumber(8))