from data_structure.Stack import MaxStack
from data_structure.Queue import StackQueue, QueueException


class MaxStackQueue(StackQueue):
    def __init__(self):
        super().__init__(MaxStack)

    def max(self):
        if self._in_stack.empty() and self._out_stack.empty():
            raise QueueException('Empty queue.')
        elif self._out_stack.empty():
            return self._in_stack.max()
        elif self._in_stack.empty():
            return self._out_stack.max()
        else:
            return max(self._in_stack.max(), self._out_stack.max())


if __name__ == '__main__':
    max_stack_queue = MaxStackQueue()
    for i in (17, 19, 100, 3, 36):
        max_stack_queue.enqueue(i)

    assert max_stack_queue.max() == 100
    assert max_stack_queue.dequeue() == 17
    assert max_stack_queue.dequeue() == 19
    assert max_stack_queue.dequeue() == 100
    assert max_stack_queue.max() == 36
