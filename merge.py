def merge_sort(lst):
    n = len(lst)
    if n == 1:
        return lst.copy()
    
    #
    # 1. 分割
    #
    left = merge_sort(lst[:n // 2])
    right = merge_sort(lst[n // 2:])
    
    #
    # 2. 統合
    #
    new_lst = []
    left.reverse()  # *補足
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
