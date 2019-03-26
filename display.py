def show_sample(sort, n):
    import random
    lst = [random.randint(0, 99) for _ in range(n)]
    print(str.join(' ', (f'{d:2d}' for d in lst)))
    sort(lst)
    print(str.join(' ', (f'{d:2d}' for d in lst)))


def print_progress(progress, lst, *args):
    assert all(0 <= e <= 99 for e in lst),\
        "Values are allowed between 0 and 99."
    print(str.join(' ', (f'{e:2d}' for e in lst)))
    print(str.join(' ', progress(lst, *args)))
    print()


def no_side_effect(sort):
    def sorted_(lst):
        new_lst = lst.copy()
        sort(new_lst)
        return new_lst

    # comparison.py で使う
    # funcscale.py が関数名を読み込むため
    sorted_.__name__ = sort.__name__
    return sorted_
