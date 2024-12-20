from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def route_finder(root: TreeNode, node_a_val: int, node_b_val: int) -> List[str]:
    def dfs(node: TreeNode, search_val: int):
        if node: print(node.val)
        if not node:
            return False, []
        if (node.val == search_val):
            return True, []
        left_ans = dfs(node.left, search_val)
        if left_ans[0]:
            return True, ['left'] + left_ans[1]
        right_ans = dfs(node.right, search_val)
        if right_ans[0]:
            return True, ['right'] + right_ans[1]
        return False, []

    solution = []
    path_to_node_a = dfs(root, node_a_val)
    path_to_node_b = dfs(root, node_b_val)

    if not path_to_node_a[0] or not path_to_node_b[0]:
        return solution

    path_a = path_to_node_a[1]
    path_b = path_to_node_b[1]

    print(path_a, path_b)
    step = 0
    for step, (a_node, b_node) in enumerate(zip(path_a, path_b)):
        if a_node != b_node:
            break

    n_ups = len(path_a) - step
    if n_ups > 0:
        solution = ['up'] * n_ups

    divergence_step = len(path_b) - step
    solution += path_b[-divergence_step:]

    return solution


root = TreeNode(5,
    TreeNode(
        3,
        TreeNode(
            6,
            TreeNode(8),
            TreeNode(9),
        ),
        TreeNode(7)
    ),
    TreeNode(4)
)


def test_route():
    assert route_finder(root, 5, 8) == ['left', 'left', 'left']
    assert route_finder(root, 7, 4) == ['up', 'up', 'right']
    assert route_finder(root, 3, 9) == ['left', 'right']

test_route()