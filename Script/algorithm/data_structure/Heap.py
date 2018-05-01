from operator import gt


class Heap:
    def __init__(self, heap, operator=gt):
        self._operator = operator  # default gt for max root heap
        self.heap = heap
        self.build_heap()

    def build_heap(self):
        for position in reversed(range(len(self.heap) // 2)):
            self._shift_down(position)

    def _shift_down(self, position):
        while not self.is_leaf(position):
            left_child_position, right_child_position = (position << 1) + 1, (position << 1) + 2
            if right_child_position < len(self.heap) and \
                    self._operator(self.heap[right_child_position], self.heap[left_child_position]):
                compare_position = right_child_position
            else:
                compare_position = left_child_position

            if self._operator(self.heap[position], self.heap[compare_position]):
                return

            self.heap[position], self.heap[compare_position] = self.heap[compare_position], self.heap[position]
            position = compare_position

    def is_leaf(self, position):
        """True is position in heap is a leaf"""
        return len(self.heap) / 2 <= position < len(self.heap)

    def replace(self, value):
        self.heap[0] = value
        self._shift_down(0)

    def top(self):
        return self.heap[0]


if __name__ == '__main__':
    a = Heap(list(range(1, 8)))
    print(a.heap)
    a.replace(2)
    print(a.heap)
