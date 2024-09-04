def goodNodes(self, root) -> int:
    # dfs approach
    # init walk with node and its val as the current max
    # the recursive walk returns the number of good nodes res
    # considered good if the current node val is bigger tan current max val that's been passed down alongside it
    # repeat left and right subtree, return back up
    def dfs(node, max_val):
        if not node:
            return 0

        if node.val >= max_val:
            res = 1  # each res var scoped to its own recursive iteration
            max_val = node.val
        else:
            res = 0
        res += dfs(node.left, max_val)
        res += dfs(node.right, max_val)

        return res

    return dfs(root, root.val)
