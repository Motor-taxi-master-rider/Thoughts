from queue import Queue


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    if not root:
        return ''
    queue = Queue()
    queue.put(root)
    output = ''
    while not queue.empty():
        node = queue.get()
        if not node:
            output += 'null,'
            continue
        output += f'{node.val},'
        queue.put(node.left)
        queue.put(node.right)
    return output[:-1]


def deserialize(string):
    if string == '':
        return None
    node_strings = string.split(',')

    queue = Queue()
    root = Node(int(node_strings[0]))
    queue.put(root)

    i = 1
    while i < len(node_strings) and not queue.empty():
        node = queue.get()

        item = node_strings[i]
        i += 1
        if item != 'null':
            node.left = Node(int(item))
            queue.put(node.left)

        if i >= len(node_strings):
            break

        item = node_strings[i]
        i += 1
        if item != 'null':
            node.right = Node(int(item))
            queue.put(node.right)
    return root


def equal(root, another_root):
    if root is None and another_root is None:
        return True
    if root is None or another_root is None:
        return False

    mid_equal = root.val == another_root.val
    left_equal = equal(root.left, another_root.left)
    right_equal = equal(root.right, another_root.right)
    return mid_equal and left_equal and right_equal


if __name__ == '__main__':
    root = Node(2)
    root.left, root.right = Node(7), Node(5)
    root.left.left, root.left.right = Node(2), Node(6)
    root.right.right = Node(9)
    root.left.right.left, root.left.right.right = Node(5), Node(11)
    root.right.right.left = Node(4)

    assert equal(root, deserialize(serialize(root)))
