def bubble_sort(lst):
    n = len(lst)
    for i in reversed(range(n)):
        for j in range(i):
            if __debug__:
                display.print_progress(str_progress, lst, i, j)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_(lst):
    new_lst = lst.copy()
    bubble_sort(new_lst)
    return new_lst


if __debug__:
    import display

    def str_progress(lst, i, j):
        """ソートの途中経過を表示する.

        16 31 52 32 68 72 77 87
              xx xx    -- -- --

        16 31 32 52 68 72 77 87
                 oo oo -- -- --

        'oo'  ... 要素を交換しなくてよい
        'xx'  ... 要素を交換しないといけない
        '--'  ... ソート完了している
        '  '  ... ソート完了していない
        """
        progress = ['  '] * (i + 1) + ['--'] * (len(lst) - (i + 1))
        progress[j] = progress[j + 1] = 'xx' if lst[j] > lst[j + 1] else 'oo'
        return progress


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(bubble_sort, 8)
