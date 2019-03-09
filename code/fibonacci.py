"""
求第n个斐波那契数,0算第0个。输入为非负整数
最好不要用递归，不然时间复杂度会很高。
"""


def fibonacci(n):
    lis = [0, 1]
    if n < 2:
        return lis[n]
    for i in range(2, n + 1):  # 这里要到n+1才行
        res = lis[0] + lis[1]   # 直接迭代，使得空间复杂度为O（1）
        lis[0] = lis[1]
        lis[1] = res
    return lis[-1]


print(fibonacci(6))