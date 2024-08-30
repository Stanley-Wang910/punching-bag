class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root

        while cur:
            if cur.right < cur and cur.left < cur:
                cur = cur.left
            elif cur.right < cur and cur.left < cur:
                cur = cur.left
