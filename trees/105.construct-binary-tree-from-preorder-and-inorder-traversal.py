def buildTree(self, preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if len(preorder) == 0:
        return None
    value = preorder.pop(0)
    l, r = self.split_array(inorder, value)
    print(l, r)

    l_tree = None if not l else self.buildTree(preorder, l)
    r_tree = None if not r else self.buildTree(preorder, r)

    return TreeNode(value, l_tree, r_tree)


def split_array(self, arr, value):
    i = 0
    while arr[i] != value:
        i += 1
    return arr[0:i], arr[i + 1 : len(arr)]
