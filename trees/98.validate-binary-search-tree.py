def isValidBST(self, root: Optional[TreeNode]) -> bool:
    def valid(node, left, right):
        if not node:
            return True
        if not (left < node.val < right):
            return False
        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    left, right = float("-inf"), float("inf")
    return valid(root, left, right)
