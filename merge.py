def merge_sort(lst):
    # ポイント
    #   マージソートは速いけど
    #   len(lst) 個分のメモリ memory を必要とします。
    memory = [None] * len(lst)  # <--- ポイント
    begin = 0
    end = len(lst) - 1
    _merge_sort(lst, memory, begin, end)


def _merge_sort(lst, memory, begin, end):
    if begin == end:
        return

    #
    # 1. ソート
    #
    mid = begin + (end - begin) // 2
    _merge_sort(lst, memory, begin, mid)
    _merge_sort(lst, memory, mid + 1, end)

    if __debug__:
        display.print_progress(str_progress, lst, begin, end)

    #
    # 2. コピー
    #
    for i in range(begin, end + 1):
        memory[i] = lst[i]

    #
    # 3. 結合
    #
    left, index, right = begin, begin, mid + 1
    while (left <= mid) and (right <= end):
        if memory[left] <= memory[right]:
            lst[index] = memory[left]
            left = left + 1
        else:
            lst[index] = memory[right]
            right = right + 1
        index = index + 1

    while left <= mid:
        lst[index] = memory[left]
        left = left + 1
        index = index + 1

    while right <= mid:
        lst[index] = memory[right]
        right = right + 1
        index = index + 1


if __debug__:
    import display

    def str_progress(lst, begin, end):
        """ソートの途中経過を表示する.

        36 42 54 77 12 45 30 44
                    << << >> >>

        36 42 54 77 12 30 44 45
        << << << << >> >> >> >>

        12 30 36 42 44 45 54 77

        << ... 左のソート済みのリスト
        >> ... 右のソート済みのリスト

        下段に行くとマージされる。
        """
        n = len(lst)
        mid = begin + (end - begin) // 2
        progress = []
        progress = progress + ['  '] * begin
        progress = progress + ['<<'] * (mid - begin + 1)
        progress = progress + ['>>'] * (end - mid)
        progress = progress + ['  '] * (n - end - 1)
        return progress


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(merge_sort, 8)
