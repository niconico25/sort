if __debug__:
    raise Exception('\n'.join((
        '-O is required.',
        '',
        '',
        '$ python3 -O comparison.py'
        '',
        '',
        '',
    )))
else:
    try:
        from comparison_of_python_code import funcscale
    except ModuleNotFoundError as err:
        url = 'https://github.com/niconico25/comparison_of_python_code/'
        print('%s: %s' % (err.__class__.__name__, str(err)))
        print('Please download...')
        print('$ git clone', url)
        import sys
        sys.exit()

    import random
    from display import no_side_effect
    from bubble import bubble_sort
    from insertion import insertion_sort
    from quick import quick_sort
    from merge import merge_sort
    from heap import heap_sort
    from linked_quick import linked_quick_sort
    from linked_merge import linked_merge_sort
    from linked_heap import linked_heap_sort


# funcscale.py では
# 計測対象の関数をグローバル変数として
# 定義しないといけないので、ここでデコレートする。
bubble_sort = no_side_effect(bubble_sort)
insertion_sort = no_side_effect(insertion_sort)
quick_sort = no_side_effect(quick_sort)
linked_quick_sort = no_side_effect(linked_quick_sort)
merge_sort = no_side_effect(merge_sort)
linked_merge_sort = no_side_effect(linked_merge_sort)
heap_sort = no_side_effect(heap_sort)
linked_heap_sort = no_side_effect(linked_heap_sort)


def comparison():
    funcscale.function_list = [
        bubble_sort,
        insertion_sort,
        quick_sort,
        linked_quick_sort,
        merge_sort,
        linked_merge_sort,
        heap_sort,
        linked_heap_sort,
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**i) for _ in range(10**i)], ), {})
        for i in range(1, 4)
    ]
    funcscale.str_argument_list = [
        f'[randint(0, 10**{i}) for i in range(0, 10**{i})]'
        for i in range(1, 4)
    ]
    funcscale.compare()


comparison()
