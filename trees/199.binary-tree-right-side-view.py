import collections


def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        q_len = len(q)
        level = []
        for i in range(q_len):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level[-1])
    return res
