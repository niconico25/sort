def quick_sort(lst):
    sorted_lst = quick_sort_(lst)
    lst.clear()
    lst.extend(sorted_lst)


def quick_sort_(lst):
    if not lst:
        return []

    center = lst.pop()
    left_list = quick_sort_([e for e in lst if e <= center])
    right_list = quick_sort_([e for e in lst if center < e])
    return left_list + [center] + right_list
