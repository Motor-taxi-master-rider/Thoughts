from data_structure import build_tree_from_list


def lowest_common_ancestor(tree, x, y):
    x_stack = _find_path(tree, x)
    y_stack = _find_path(tree, y)
    result = None
    while x_stack and y_stack:
        x_result = x_stack.pop()
        y_result = y_stack.pop()
        if x_result == y_result:
            result = x_result
        else:
            break
    return result


def _find_path(root, value):
    if not root:
        return None
    if root.value == value:
        return [value]
    left_path = _find_path(root.left, value)
    if left_path:
        left_path.append(root.value)
        return left_path
    right_path = _find_path(root.right, value)
    if right_path:
        right_path.append(root.value)
        return right_path
    return None


if __name__ == '__main__':
    array = range(1, 15)
    root = build_tree_from_list(array)
    assert lowest_common_ancestor(root, 5, 8) == 2
    assert lowest_common_ancestor(root, 8, 14) == 1
    assert lowest_common_ancestor(root, 12, 13) == 6
    assert lowest_common_ancestor(root, 12, 12) == 12
    assert lowest_common_ancestor(root, 12, 15) is None
    assert _find_path(root, 14) == [14, 7, 3, 1]
    assert _find_path(root, 1) == [1]
    assert _find_path(root, 15) is None
