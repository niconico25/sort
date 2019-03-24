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
from bubble import bubble_sort_
from insertion import insertion_sort_
from merge import merge_sort_
from merge_difficult import merge_sort_difficult_
from quick import quick_sort_
from quick_difficult import quick_sort_difficult_
from heap import heap_sort_
from heap_difficult import heap_sort_difficult_


def comparison():
    funcscale.function_list = [
        bubble_sort_,
        insertion_sort_,
        merge_sort_,
        merge_sort_difficult_,
        quick_sort_,
        quick_sort_difficult_,
        heap_sort_,
        heap_sort_difficult_,
    ]
    funcscale.argument_list = [
        (([random.randint(0, 10**i) for _ in range(10**i)], ), {})
        for i in range(4)
    ]
    funcscale.str_argument_list = [
        f'[randint(0, 10**{i}) for i in range(0, 10**{i})]'
        for i in range(4)
    ]
    funcscale.compare()


comparison()
