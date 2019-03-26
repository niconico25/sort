def quick_sort_difficult(lst):
    # ポイント
    #   クイックソートは速いけど
    #   len(lst) 個分のメモリ memory を必要とします。
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
    lst[left] = pivod

    if __debug__:
        pivot_index = left
        display.print_progress(progress, lst, begin, pivot_index, end)

    _quick_sort_difficult(lst, memory, begin, left - 1)
    _quick_sort_difficult(lst, memory, right + 1, end)


def quick_sort_difficult_(lst):
    new_lst = lst.copy()
    quick_sort_difficult(new_lst)
    return new_lst


if __debug__:
    import display

    def progress(lst, begin, pivot_index, end):
        n = len(lst)
        progress = []
        progress = progress + ['  '] * begin
        progress = progress + ['<<'] * (pivot_index - begin)
        progress = progress + ['pv']
        progress = progress + ['>>'] * (end - pivot_index)
        progress = progress + ['  '] * (n - end - 1)
        return progress


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(quick_sort_difficult, 16)
