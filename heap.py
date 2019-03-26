def heap_sort(lst):
    # ポイント
    #   ヒープソートは、マージソートやクイックソートのように
    #   len(lst) 個分のメモリ memory を必要としません。

    # 1) リストをヒープにする。
    heapify(lst)

    # 2) ヒープの先頭を取り出し、リストの末尾に付け足す。
    index = len(lst) - 1
    while index:
        lst[0], lst[index] = lst[index], lst[0]
        _siftup(lst, 0, index)
        index = index - 1

    # 3) 逆さまなので反転させる。
    lst.reverse()


#
# heapq.py
# https://github.com/python/cpython/blob/3.7/Lib/heapq.py
#
#   そのまま from heapq import ... してしまうと
#   C 言語実装の heapq が import されて鬼のように速くなるので
#   heapq.py からコピペ
#
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


# heapq._siftup を
# 先頭の２行だけを書き換えました。
#
# - def _siftup(heap, pos):
# -     endpos = len(heap)
# + def _siftup(heap, pos, endpos):
# +     # endpos = len(heap)
#
def _siftup(heap, pos, endpos):
    startpos = pos
    newitem = heap[pos]
    childpos = 2 * pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


# heapq._heapify を
# 書き換え
#
# - _siftup(x, i)
# + _siftup(x, i, n)
#
def heapify(x):
    n = len(x)
    for i in reversed(range(n // 2)):
        _siftup(x, i, n)


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(heap_sort, 8)
