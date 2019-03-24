def merge_sort(lst):
    sorted_lst = merge_sort_(lst)
    lst.clear()
    lst.extend(sorted_lst)


def merge_sort_(lst):
    n = len(lst)
    if n == 1:
        return lst.copy()

    #
    # 1. 分割
    #
    left = merge_sort_(lst[:n // 2])
    right = merge_sort_(lst[n // 2:])

    #
    # 2. 統合
    #
    new_lst = []
    left.reverse()
    right.reverse()
    while left and right:
        if left[-1] <= right[-1]:
            new_lst.append(left.pop())
        else:
            new_lst.append(right.pop())

    while left:
        new_lst.append(left.pop())

    while right:
        new_lst.append(right.pop())

    return new_lst
