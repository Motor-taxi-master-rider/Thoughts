from typing import Union


class StackException(Exception):
    pass


class MaxStack:
    def __init__(self):
        self._elements = []
        self._maximums = []

    def empty(self):
        return len(self._elements) == 0

    def push(self, item: Union[int, float]):
        if not self._maximums:
            self._maximums.append(item)
        else:
            if item > self._maximums[-1]:
                self._maximums.append(item)
            else:
                self._maximums.append(self._maximums[-1])
        self._elements.append(item)

    def pop(self):
        if self.empty():
            raise StackException('Empty stack.')
        self._maximums.pop()
        return self._elements.pop()

    def top(self):
        if self.empty():
            raise StackException('Empty stack.')
        return self._elements[-1]

    def max(self):
        if self.empty():
            raise StackException('Empty stack.')
        return self._maximums[-1]


def is_stack_class(stack_class):
    import logging
    from inspect import isclass

    if not isclass(stack_class):
        raise TypeError(f'Expected type Class, given {type(stack_class)}')

    for method in ('push', 'pop', 'empty', 'top'):
        if not hasattr(stack_class, method):
            logging.error(f'{stack_class} has no attribute {method}.')
            return False
    return True


if __name__ == '__main__':
    max_stack = MaxStack()
    for i in range(10):
        max_stack.push(i)

    assert max_stack.max() == 9
    assert max_stack.pop() == 9
    assert max_stack.max() == 8

    assert is_stack_class(MaxStack)
