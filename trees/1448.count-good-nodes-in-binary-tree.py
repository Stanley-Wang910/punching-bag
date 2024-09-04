import collections


def goodNodes(self, root):
    q = collections.deque()
    q.append(root)
    res = []

    while q:
        right_node = None
        len_q = len(q)
        for i in range(len_q):
            node = q.popleft()
            if node:
                right_node = node
                q.append(node.left)
                q.append(node.right)

        if right_node:
            res.append(right_node.val)
    return res
