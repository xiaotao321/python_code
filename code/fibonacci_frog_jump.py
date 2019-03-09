"""
问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。
求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）
输入为正整数

和斐波那契数列类似，有递推公式f(n) = f(n-1) + f(n-2)
最好不要用递归，不然时间复杂度会很高。使用循环要好一些
"""


def fibonacci_frog_jump(n):
    lis = [1, 2]
    if n <= 2:
        return lis[n-1]
    for i in range(2, n):
        res = lis[0] + lis[1]  # 直接迭代，使得空间复杂度为O（1）
        lis[0] = lis[1]
        lis[1] = res
    return lis[-1]


print(fibonacci_frog_jump(6))