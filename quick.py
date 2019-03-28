def quick_sort(lst):
    _quick_sort(lst, 0, len(lst) - 1)


def _quick_sort(lst, begin, end):
    if begin == end + 1:
        return

    #
    # 1. 分割
    #
    left, right = begin, end - 1
    pivot = lst[end]
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

    # right = right if 0 <= right else left
    lst[left], lst[end] = lst[end], lst[left]
    pivot_index = left

    if __debug__:
        display.print_progress(progress, lst, begin, pivot_index, end)

    #
    # 2. ソート
    #
    _quick_sort(lst, begin, pivot_index - 1)
    _quick_sort(lst, pivot_index + 1, end)


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
