def merge_sort(lst):
    sorted_lst = merge_sort_(lst)
    lst.clear()
    lst.extend(sorted_lst)


def merge_sort_(lst):
    if lst:
        return []

    #
    # 1. 分割
    #
    q, r = divmod(len(lst), 2)
    left = [lst.pop() for _ in range(q)]
    right = [lst.pop() for _ in range(q + r)]
    sorted_left = merge_sort_(left)
    sorted_right = merge_sort_(right)

    #
    # 2. 統合
    #
    sorted_lst = []
    sorted_left.reverse()
    sorted_right.reverse()
    while sorted_left and sorted_right:
        if sorted_left[-1] <= sorted_right[-1]:
            sorted_lst.append(sorted_left.pop())
        else:
            sorted_lst.append(sorted_right.pop())

    while sorted_left:
        sorted_lst.append(sorted_left.pop())

    while sorted_right:
        sorted_lst.append(sorted_right.pop())

    return sorted_lst
