def linked_heap_sort(lst):
    heap = []
    while lst:
        heappush(heap, lst.pop())
        if __debug__:
            print_progress(lst, heap)
    while heap:
        lst.append(heappop(heap))
        if __debug__:
            print_progress(lst, heap)


#
# heapq.py
# https://github.com/python/cpython/blob/3.7/Lib/heapq.py
#
#   そのまま from heapq import ... してしまうと
#   C 言語実装の heapq が import されて鬼のように速くなるので
#   heapq.py からコピペ
#
def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap) - 1)


def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
# is the index of a leaf with a possibly out-of-order value.  Restore the
# heap invariant.
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2 * pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2 * pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


if __debug__:
    try:
        from tree.tree.binary_heap import BinaryHeap
    except ModuleNotFoundError as err:
        url = 'https://github.com/niconico25/tree'
        print('%s: %s' % (err.__class__.__name__, str(err)))
        print(__file__)
        print('Please download...')
        print('$ git clone', url)
        import sys
        sys.exit()

    def print_progress(lst, heap):
        print(lst)
        print(BinaryHeap(heap))
        print()


if __name__ == '__main__':
    import display  # noqa
    display.show_sample(linked_heap_sort, 7)
