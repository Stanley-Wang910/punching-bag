def goodNodes(self, root) -> int:
    def dfs(node, max_val):
        if not node:
            return 0
        num_good = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)

        num_good += dfs(node.right, max_val)
        num_good += dfs(node.left, max_val)

        return num_good

    return dfs(root, root.val)
