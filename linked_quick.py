def linked_quick_sort(lst):
    if not lst:
        return
    #
    # 1. 分割
    #
    smaller = []
    pivot = lst.pop()
    bigger = []
    while lst:
        e = lst.pop()
        if e <= pivot:
            smaller.append(e)
        else:
            bigger.append(e)

    #
    # 2. ソート
    #
    linked_quick_sort(smaller)
    linked_quick_sort(bigger)

    #
    # 3. 結合
    #
    smaller.reverse()
    while smaller:
        lst.append(smaller.pop())
    lst.append(pivot)
    bigger.reverse()
    while bigger:
        lst.append(bigger.pop())


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(linked_quick_sort, 8)
