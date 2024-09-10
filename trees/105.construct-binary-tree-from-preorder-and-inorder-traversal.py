def buildTree(self, preorder, inorder):
    #     """
    #     :type preorder: List[int]
    #     :type inorder: List[int]
    #     :rtype: TreeNode
    #     """
   if len(preorder) == 0:
        return None

    val = preorder.pop(0)
    m = inorder.index(val)
    l, r = inorder[:m], inorder[m+1:]
    l_tree = None if len(l) == 0 else self.buildTree(preorder, l)
    r_tree = None if len(r) == 0 else self.buildTree(preorder, r)
    return TreeNode(val, l_tree, r_tree)
