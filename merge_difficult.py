def merge_sort_difficult(lst):
    # ポイント
    #   マージソートは速いけど
    #   len(lst) 個分のメモリを必要とします。
    memory = [None] * len(lst)  # <--- ポイント
    begin = 0
    end = len(lst) - 1
    _merge_sort_difficult(lst, memory, begin, end)


def _merge_sort_difficult(lst, memory, begin, end):
    if begin == end:
        return

    #
    # 1. 分割
    #
    mid = begin + (end - begin) // 2
    _merge_sort_difficult(lst, memory, begin, mid)
    _merge_sort_difficult(lst, memory, mid + 1, end)

    #
    # 2. 統合
    #
    for i in range(begin, end + 1):
        memory[i] = lst[i]

    left, index, right = begin, begin, mid + 1
    while (left <= mid) and (right <= end):
        if memory[left] <= memory[right]:
            lst[index] = memory[left]
            left = left + 1
        else:
            lst[index] = memory[right]
            right = right + 1
        index = index + 1

    while left <= mid:
        lst[index] = memory[left]
        left = left + 1
        index = index + 1

    while right <= mid:
        lst[index] = memory[right]
        right = right + 1
        index = index + 1


def merge_sort_difficult_(lst):
    new_lst = lst.copy()
    merge_sort_difficult(new_lst)
    return new_lst
