def insertion_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in reversed(range(i)):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            else:
                break  # <- この break 文がポイント