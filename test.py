"""Tsting sort algorithm.

概要
    test 関数は、0 ~ 99 のランダムな 100 個の整数を
    正しくソートできるかを 100 回確認させています。

実行
    $ python -O test.py
    Test was succeeded
    $

関連
* [Python の assert 文でテストする](https://python.ms/sub/misc/assert/)
"""
from contextlib import contextmanager
from bubble import bubble_sort_
from insertion import insertion_sort_
from merge import merge_sort_
from merge_difficult import merge_sort_difficult_
from quick import quick_sort_
from quick_difficult import quick_sort_difficult_
from heap import heap_sort_
from heap_difficult import heap_sort_difficult_


def main():
    test(bubble_sort_)
    test(insertion_sort_)
    test(merge_sort_)
    test(merge_sort_difficult_)
    test(quick_sort_)
    test(quick_sort_difficult_)
    test(heap_sort_)
    test(heap_sort_difficult_)

    # incorrect_sort は
    # shuffle してるのでエラーになる。
    # 正しくテストできているかを確認するために、
    # 意図的にエラーを起こしています。
    try:
        # print 関数を無効にする。
        with suppress_print():
            test(incorrect_sort)
    except AssertionError:
        pass

    print('Test was succeeded.')


def test(sort):
    from random import randint
    for _ in range(100):
        lst = [randint(0, 99) for _ in range(100)]
        new_lst = sort(lst)
        assert is_sorted(new_lst), f'{sort.__name__} is incorrect.'


def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def incorrect_sort(lst):
    # ソートしたと見せかけて
    new_lst = sorted(lst)
    # 一部、値を入れ替えてソートを崩す。
    from random import randint
    i = j = 0
    while new_lst[i] == new_lst[j]:
        i, j = randint(0, 99), randint(0, 99)
    new_lst[i], new_lst[j] = new_lst[j], new_lst[i]
    return new_lst


# with 文と @contextlib.contextmanager が便利
# https://qiita.com/QUANON/items/c5868b6c65f8062f5876
@contextmanager
def suppress_print():
    # Suppress calls to print (python) - Stackoverflow
    # https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
    import sys
    import io
    stdout = sys.stdout
    sys.stdout = io.StringIO()
    try:
        yield
    finally:
        sys.stdout = stdout


if __debug__:
    raise Exception('\n'.join((
        '-O is required.',
        '',
        '',
        '$ python3 -O test.py'
        '',
        '',
        '',
    )))
else:
    main()
