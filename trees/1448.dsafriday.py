def goodNodes(self, root: TreeNode) -> int:

    def dfs(node, cur_max):
        if not node:
            return 0
        count = 1 if node.val >= max.val else 0
        cur_max = max(node.val, max.val)

        left_count = dfs(node.left, cur_max)
        right_count = dfs(node.right, cur_max)

        return left_count + right_count + count

    dfs(root, root.val)
