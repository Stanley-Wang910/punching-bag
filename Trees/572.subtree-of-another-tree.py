class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        elif not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot)
        or self.isSubtree(root.right, subRoot))


    def sameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q or p.val != q.val:
            return False

        return (self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right))
asidbasiudbasiudb
