def bubble_sort(lst):
    n = len(lst)
    for i in reversed(range(n)):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
