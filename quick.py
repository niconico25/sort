def quick_sort(lst):
    # ポイント
    #   クイックソートは速いけど
    #   len(lst) 個分のメモリ memory を必要とします。
    memory = [None] * len(lst)  # <--- ポイント
    begin = 0
    end = len(lst) - 1
    _quick_sort(lst, memory, begin, end)


def _quick_sort(lst, memory, begin, end):
    if begin == end + 1:
        return

    #
    # 1. コピー
    #
    for i in range(begin, end + 1):
        memory[i] = lst[i]

    #
    # 2. 分割
    #
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

    #
    # 3. ソート
    #
    _quick_sort(lst, memory, begin, left - 1)
    _quick_sort(lst, memory, right + 1, end)


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
    display.show_sample(quick_sort, 16)
