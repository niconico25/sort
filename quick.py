def quick_sort(lst):
    sorted_lst = quick_sort_(lst)
    lst.clear()
    lst.extend(sorted_lst)


def quick_sort_(lst):
    if not lst:
        return []

    pivot = lst.pop()
    smaller = []
    bigger = []
    while lst:
        e = lst.pop()
        if e <= pivot:
            smaller.append(e)
        else:
            bigger.append(e)

    sorted_smaller = quick_sort_(smaller)
    sorted_bigger = quick_sort_(bigger)
    return sorted_smaller + [pivot] + sorted_bigger
