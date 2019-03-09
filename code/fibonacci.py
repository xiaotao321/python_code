def fibonacci(n):
    """
    求第n个斐波那契数,0算第0个。
    最好不要用递归，不然时间复杂度会很高。
    """
    lis = [0, 1, 1]
    if n < 3:
        return lis[n]
    for i in range(3, n + 1):  # 这里要到n+1才行
        lis = [lis[1], lis[2], lis[1]+lis[2]]  # 直接迭代，使得空间复杂度为O（1）
    return lis[-1]


print(fibonacci(6))