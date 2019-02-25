'''
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
'''
'''
贪心算法：首位双指针，窗口思想：大于s去掉beg,小于s加入end。
'''
class Solution():
    def FindContinuousSequence(self, s):
        beg = 1
        end = 2
        out = []
        while end and beg:
            out.extend(list(range(beg, end + 1)))
            ssum = sum(out)
            if ssum == s:
                return out
            if ssum < s:
                end += 1
            if ssum > s:
                beg -= 1
s= Solution()
print(s.FindContinuousSequence(100))
