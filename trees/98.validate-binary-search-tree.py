def isValidBST(self, root: Optional[TreeNode]) -> bool:
    # Need to confirm at each point is less / greater than left, right
    def dfs(node, left, right):
        if not node:
            return True

        if not (left < node.val < right):
            return False

        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

    return dfs(root, float("-inf"), float("inf"))
