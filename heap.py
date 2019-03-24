def heap_sort(lst):
    # 1) ヒープ heap を作成
    heapify(lst)
    heap = lst

    # 2) 先頭を取り出し末尾と取り替え
    bottom = len(heap) - 1
    while bottom:
        heap[0], heap[bottom] = heap[bottom], heap[0]
        _siftup(heap, 0, bottom)
        bottom = bottom - 1
    heap.reverse()


def heap_sort_(lst):
    new_lst = lst.copy()
    heap_sort(new_lst)
    return new_lst


#
# heapq.py
#   そのまま from heapq import heappop してしまうと
#   C 言語実装の heapop が import されて鬼のように速くなるので
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
