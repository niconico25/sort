def linked_merge_sort(lst):
    if len(lst) == 1:
        return

    #
    # 1. 分割
    #
    q, r = divmod(len(lst), 2)
    left = [lst.pop() for _ in range(q)]
    right = [lst.pop() for _ in range(q + r)]

    #
    # 2. ソート
    #
    linked_merge_sort(left)
    linked_merge_sort(right)

    #
    # 3. 統合
    #
    left.reverse()
    right.reverse()
    while left and right:
        if left[-1] <= right[-1]:
            lst.append(left.pop())
        else:
            lst.append(right.pop())
    while left:
        lst.append(left.pop())
    while right:
        lst.append(right.pop())


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(linked_merge_sort, 8)
