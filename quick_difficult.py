def quick_sort_difficult(lst):
    # ポイント
    #   クイックソートは速いけど
    #   len(lst) 個のメモリ memory を必要とします。
    memory = [None] * len(lst)  # <--- ポイント
    begin = 0
    end = len(lst) - 1
    _quick_sort_difficult(lst, memory, begin, end)


def _quick_sort_difficult(lst, memory, begin, end):
    if begin == end + 1:
        return

    for i in range(begin, end + 1):
        memory[i] = lst[i]

    left, index, right = begin, begin, end
    pivod = memory[end]
    while index < end:
        if memory[index] < pivod:
            lst[left] = memory[index]
            left = left + 1
        else:
            lst[right] = memory[index]
            right = right - 1
        index = index + 1

    _quick_sort_difficult(lst, memory, begin, left - 1)
    lst[left] = pivod
    _quick_sort_difficult(lst, memory, right + 1, end)


def quick_sort_difficult_(lst):
    new_lst = lst.copy()
    quick_sort_difficult(new_lst)
    return new_lst
