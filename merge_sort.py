def merge_sort(lst):
    # ポイント
    #   マージソートは速いけど
    #   [None] * len(lst) 分のメモリを必要とします。
    tmp_lst = [None] * len(lst)  # <- ポイント
    begin = 0
    end = len(lst) - 1
    _merge_sort(lst, tmp_lst, begin, end)


def _merge_sort(lst, tmp_lst, begin, end):
    if begin == end:
        return
    
    #
    # 1. 分割
    #
    mid = begin + (end - begin) // 2
    _merge_sort(lst, tmp_lst, begin, mid)
    _merge_sort(lst, tmp_lst, mid + 1, end)
    
    #
    # 2. 統合
    #
    for i in range(begin, end + 1):
        tmp_lst[i] = lst[i]
    
    index = begin
    left = begin
    right = mid + 1
    while (left <= mid) and (right <= end):
        if tmp_lst[left] <= tmp_lst[right]:
            lst[index] = tmp_lst[left]
            left = left + 1
        else:
            lst[index] = tmp_lst[right]
            right = right + 1
        index = index + 1
    
    while left <= mid:
        lst[index] = tmp_lst[left]
        left = left + 1
        index = index + 1
    
    while right <= mid:
        lst[index] = tmp_lst[right]
        right = right + 1
        index = index + 1
