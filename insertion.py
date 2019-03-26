def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in reversed(range(i)):
            if __debug__:
                display.print_progress(str_progress, lst, i, j)
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
            else:
                break  # <- この break 文がポイント


if __debug__:
    import display

    def str_progress(lst, i, j):
        """ソートの途中経過を表示する.

        18 60 81 65 94 24 23 34
              xx xx    -- -- --

        18 60 65 81 94 24 23 34
           oo oo       -- -- --

        'oo'  ... 要素を交換しなくてよい
        'xx'  ... 要素を交換しないといけない
        '--'  ... まだ１度も比較していない
        '  '  ... １度は比較した
        """
        progress = ['  '] * (i + 1) + ['--'] * (len(lst) - (i + 1))
        progress[j] = progress[j + 1] = 'xx' if lst[j] > lst[j + 1] else 'oo'
        return progress

if __name__ == '__main__':
    import display  # noqa
    display.show_sample(insertion_sort, 8)
