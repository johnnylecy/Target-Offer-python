"""
题目描述
一只青蛙一次可以跳上1级台阶，
也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
"""
"""
常规想法是每一步都可两种可能，但没有递归边界。所以从最后一步两种可能逆推递归
"""

def ttj(n):
    if n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 2
    elif n > 2:
        return ttj(n-1) + ttj(n-2)

if __name__ == "__main__":
    print(ttj(4))
