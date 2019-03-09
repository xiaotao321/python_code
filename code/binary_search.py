"""
寒武纪笔试题，二分查找，给一有序列表lis，没有重复元素，给一个数num，找到就返回下标，找不到返回False
思考，如果有重复元素，该如何操作。
"""


def bin_search(lis, num):
    low = 0
    high = len(lis)-1
    while low <= high:    # 注意这里，有没有等于
        mid = (low + high) // 2  # 向下取整
        if lis[mid] == num:
            return mid
        elif lis[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return False


print(bin_search(range(10), 9))
