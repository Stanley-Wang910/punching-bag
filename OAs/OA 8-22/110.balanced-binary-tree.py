#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True, 0]
            
            left_b, left = dfs(root.left)
            right_b, right = dfs(root.right)

            diff = abs(left - right)

            balanced = (left_b and right_b) and (diff <= 1)
            return [balanced, max(left, right) + 1]
        
        balanced, height = dfs(root)
        return balanced
        
# @lc code=end

