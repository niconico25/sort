def quick_sort(lst):
    sorted_lst = quick_sort_(lst)
    lst.clear()
    lst.extend(sorted_lst)


def quick_sort_(lst):
    if not lst:
        return []
    #
    # 1. 分割
    #
    pivot = lst.pop()
    smaller = []
    bigger = []
    while lst:
        e = lst.pop()
        if e <= pivot:
            smaller.append(e)
        else:
            bigger.append(e)
    
    #
    # 2. 統合
    #
    sorted_smaller = quick_sort_(smaller)
    sorted_bigger = quick_sort_(bigger)
    sorted_lst = sorted_smaller + [pivot] + sorted_bigger

    return sorted_lst


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(quick_sort, 8)
