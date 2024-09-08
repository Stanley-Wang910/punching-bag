def isBalanced(self, root: Optional[TreeNode]) -> bool:
    def dfs(node):
        if not node:
            return 0, True

        left_s, l_b = dfs(node.left)
        right_s, r_b = dfs(node.right)

        max_h = max(left_s, right_s) + 1

        return max_h, abs(left_s - right_s) <= 1 and l_b and r_b

    _, balanced = dfs(root)
    return balanced
