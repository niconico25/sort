def quick_sort_difficult(lst):
    # ポイント
    #   クイックソートは速いけど
    #   [None] * len(lst) 分のメモリを必要とします。
    tmp_lst = [None] * len(lst)  # <- ポイント
    begin = 0
    end = len(lst) - 1
    _quick_sort(lst, tmp_lst, begin, end)


def _quick_sort(lst, tmp_lst, begin, end):
    if begin >= end:
        return
    
    for i in range(begin, end + 1):
        tmp_lst[i] = lst[i]
    
    index = begin - 1
    left = begin - 1
    right = end + 1
    pivod = lst[end]
    
    # except `end`, because `end` is pivot
    while index < end - 1:
        index = index + 1
        if tmp_lst[index] < pivod:
            left = left + 1
            lst[left] = tmp_lst[index]
        else:
            right = right - 1
            lst[right] = tmp_lst[index]
    
    _quick_sort(lst, tmp_lst, begin, left)
    lst[left + 1] = pivod
    _quick_sort(lst, tmp_lst, right, end)
