class TreeNode:
    def __init__(self, left=None, right=None, value=None):
        self.left = left
        self.right = right
        self.value = value


def build_tree_from_list(lst):
    """
    use array like objects to construct a binary tree, 'None' will stand for leaf nodes
    :param lst:
    :return:
    """

    def helper(order):
        if order > len(lst):
            return None
        if lst[order - 1] is None:
            return None
        return TreeNode(left=helper(order << 1), right=helper(order << 1 | 1), value=lst[order - 1])

    return helper(1)
