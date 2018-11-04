from .Stack import is_stack_class


class QueueException(Exception):
    pass


class StackQueue:
    def __init__(self, stack):
        if not is_stack_class:
            raise TypeError('Must provide a stack like class.')
        self._in_stack = stack()
        self._out_stack = stack()

    def enqueue(self, item):
        self._in_stack.push(item)

    def dequeue(self):
        if self._out_stack.empty():
            if self._in_stack.empty():
                raise QueueException('No elements in queue.')

            while not self._in_stack.empty():
                self._out_stack.push(self._in_stack.pop())

        return self._out_stack.pop()


if __name__ == '__main__':
    from Stack import MaxStack

    stack_queue = StackQueue(MaxStack)
    for i in range(5):
        stack_queue.enqueue(i)

    for i in range(5):
        assert stack_queue.dequeue() == i
