from typing import List


class TreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value

    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return _equal(self, other)
        else:
            raise NotImplemented

    def traverse(self):
        """build tree to list with in order."""

        yield from _traverse(self)


def build_tree_from_list(lst: List):
    """
    use array like objects to construct a binary tree, 'None' will stand for leaf nodes
    :param lst:
    :return:
    """

    def helper(order):
        if order > len(lst):
            return None
        if not lst[order - 1] or lst[order - 1] == ' ':
            return None
        return TreeNode(left=helper(order << 1), right=helper(order << 1 | 1), value=lst[order - 1])

    return helper(1)


def _traverse(node: TreeNode):
    """Traverse a binary tree with in order"""
    if not node:
        return
    yield from _traverse(node.left)
    yield node.value
    yield from _traverse(node.right)


def _equal(node: TreeNode, other_node: TreeNode):
    """Two tree are same in value."""

    if not node:
        if not other_node:
            return True
        return False

    if node.value != other_node.value:
        return False

    return _equal(node.left, other_node.left) and _equal(node.right, other_node.right)
