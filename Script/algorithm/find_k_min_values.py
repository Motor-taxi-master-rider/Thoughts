from data_structure.Heap import Heap


def find_k_min_value_heap(lst, k):
    """solve with a max root heap. O(k + (n - k) * log(k))"""
    max_heap = Heap(lst[:k])
    for item in lst[k:]:
        if item < max_heap.top():
            max_heap.replace(item)

    return max_heap.heap


if __name__ == '__main__':
    lst = [4, 1, 5, 2, 3, 0, 10]
    assert set(find_k_min_value_heap(lst, 3)) == {0, 1, 2}
    assert set(find_k_min_value_heap(lst, 6)) == {0, 1, 2, 3, 4, 5}
