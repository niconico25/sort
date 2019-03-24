def bubble_sort(lst):
    n = len(lst)
    for i in reversed(range(n)):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def bubble_sort_(lst):
    new_lst = lst.copy()
    bubble_sort(new_lst)
    return new_lst
