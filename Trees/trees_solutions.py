class Trees:

    # 226. Invert Binary Tree - Easy - 7 minutes - https://leetcode.com/problems/invert-binary-tree/
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
