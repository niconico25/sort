def quick_sort(lst):
    if not lst:
        return []
    
    center     = lst.pop()
    left_list  = quick_sort([e for e in lst if e <= center])
    right_list = quick_sort([e for e in lst if center < e ])
    return left_list + [center] + right_list
