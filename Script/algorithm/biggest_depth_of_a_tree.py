from data_structure.Tree import build_tree_from_list, TreeNode


def biggest_depth_of_a_tree(root: TreeNode):
    max_distance = 0

    def helper(root: TreeNode):
        nonlocal max_distance
        if not root:
            return 0

        max_left_depth = helper(root.left)
        max_right_depth = helper(root.right)

        max_distance = max(max_distance, max_left_depth + max_right_depth)

        return max(max_left_depth, max_right_depth) + 1

    helper(root)
    return max_distance


if __name__ == '__main__':
    root = build_tree_from_list([1, 2, None, 4, 5, None, None, None, 9, 10])
    assert biggest_depth_of_a_tree(root) == 4
    root = build_tree_from_list([1])
    assert biggest_depth_of_a_tree(root) == 0
    root = build_tree_from_list([1, 2])
    assert biggest_depth_of_a_tree(root) == 1
    root = build_tree_from_list([1, 2, 3])
    assert biggest_depth_of_a_tree(root) == 2
