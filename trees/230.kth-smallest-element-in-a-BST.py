def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    # dict key depth level and value =  list of elements?
    # only need to consider the left side, as k cannot be negative
    stack = []
    cur = root

    while stack or cur:
        while cur:

