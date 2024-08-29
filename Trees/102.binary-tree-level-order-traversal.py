class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = collections.deque() # use queue struct
        res = []
        q.append(root)

        while q:
            q_len = len(q)
            level = [] # Sublist per depth level
            for i in range(q_len):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right) # These could be null
            if level:
                res.append(level)

        return res



