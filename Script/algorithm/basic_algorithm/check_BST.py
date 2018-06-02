import math

from data_structure.Tree import build_tree_from_list


def check_BST(root, low, high):
    """check a binary tree whether is BST or not"""
    if not root:
        return True
    root_value = root.value
    if not low <= root_value <= high:
        return False
    if not check_BST(root.left, low, root_value):
        return False
    return check_BST(root.right, root_value, high)


if __name__ == '__main__':
    lst = [20, None, 50, None, None, 40, 75, None, None, None, None, 21]
    test = build_tree_from_list(lst)
    assert check_BST(test, -math.inf, math.inf) == True

    lst = [20, None, 50, None, None, 40, 75, None, None, None, None, 20]
    test = build_tree_from_list(lst)
    assert check_BST(test, -math.inf, math.inf) == True

    lst = [20, None, 50, None, None, 40, 75, None, None, None, None, 19]
    test = build_tree_from_list(lst)
    assert check_BST(test, -math.inf, math.inf) == False
