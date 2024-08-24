#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Null tree is a subtree of any tree
        if not subRoot: return True
        # if subRoot tree not null, non-null tree cannot be subtree of null tree
        if not root: return False

        def isSameTree(p, q):
            # One null, the other not!
            if not p and not q:
                return True
            elif not p or not q or p.val != q.val: 
                return False
        
            # Return the AND of both bool results to determine Sameness
            return (isSameTree(p.left, q.left)) and (isSameTree(p.right, q.right))

        if isSameTree(root, subRoot):
            return True

        # If not the same tree directly, compare subtrees recursively
        return (self.isSubtree(root.left, subRoot) or
        self.isSubtree(root.right, subRoot))



        


        subTree = sameTree(root, subRoot)




        if root.val == subRoot.val:
            return (self.isSubtree(root.left, subRoot.left)) and (self.isSubtree(root.right, subRoot.right))  
        else:
            return (self.isSubtree(root.left, subRoot)) and (self.isSubtree(root.right, subRoot))  


# @lc code=end

