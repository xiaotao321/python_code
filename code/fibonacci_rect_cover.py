"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
输入为正整数

还是斐波那契数列，易得f(n)=f(n-1)+f(n-2),注意一下初始值就行了。
"""


def fibonacci_rect_cover(n):
    lis = [1, 2]
    if n <= 2:
        return lis[n-1]
    for i in range(2, n):  # 这里要到n+1才行
        res = lis[0] + lis[1]  # 直接迭代，使得空间复杂度为O（1）
        lis[0] = lis[1]
        lis[1] = res
    return lis[-1]


print(fibonacci_rect_cover(6))