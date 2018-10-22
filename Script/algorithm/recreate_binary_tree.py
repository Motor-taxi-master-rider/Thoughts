from typing import List

from data_structure.Tree import TreeNode, build_tree_from_list


def recreate_binary_tree(in_order: List[str], pre_order: List[str]):
    if not in_order or not pre_order:
        return None
    root_val = pre_order[0]
    root_index = in_order.index(root_val)
    left_in_order, right_in_order = in_order[:root_index], in_order[root_index + 1:]
    left_pre_order, right_pre_order = pre_order[1:len(left_in_order) + 1], pre_order[len(left_in_order) + 1:]
    left_tree, right_tree = recreate_binary_tree(left_in_order, left_pre_order), recreate_binary_tree(right_in_order,
                                                                                                      right_pre_order)

    root_node = TreeNode(left_tree, right_tree, root_val)
    return root_node


if __name__ == '__main__':
    tree = recreate_binary_tree(list('dbaecf'), list('abdcef'))
    assert tree == build_tree_from_list(list('abcd ef'))
