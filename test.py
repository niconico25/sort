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
    from contextlib import contextmanager
    from bubble import bubble_sort
    from insertion import insertion_sort
    from quick import quick_sort
    from merge import merge_sort
    from heap import heap_sort
    from linked_quick import linked_quick_sort
    from linked_merge import linked_merge_sort
    from linked_heap import linked_heap_sort
    from display import no_side_effect


def main():
    test(no_side_effect(bubble_sort))
    test(no_side_effect(insertion_sort))
    test(no_side_effect(merge_sort))
    test(no_side_effect(quick_sort))
    test(no_side_effect(heap_sort))
    test(no_side_effect(linked_quick_sort))
    test(no_side_effect(linked_merge_sort))
    test(no_side_effect(linked_heap_sort))

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


main()
