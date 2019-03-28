def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)


def _quick_sort(lst, begin, end):
    if begin == end + 1:
        return

    #
    # 1. 分割
    #
    left, right = begin, end
    pivot = lst[end]

    # **大事**
    #   pivot を番兵にしている
    #   これがないと right が begin を突き抜けて
    #   リストを一周してしまう
    lst[left], lst[right] = lst[right], lst[left]

    while True:
        while lst[left] < pivot:
            left = left + 1
        while pivot < lst[right]:
            right = right - 1
        if right <= left:
            break
        lst[left], lst[right] = lst[right], lst[left]
        left = left + 1
        right = right - 1

    if __debug__:
        display.print_progress(progress, lst, begin, left, end)

    #
    # 2. ソート
    #
    _quick_sort(lst, begin, left - 1)
    _quick_sort(lst, right + 1, end)


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
