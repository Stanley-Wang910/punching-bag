class Trees:

    # 226. Invert Binary Tree - Easy - 7 minutes - https://leetcode.com/problems/invert-binary-tree/
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.right)
        self.invertTree(root.left)
        return root

    # 104. Maximum Depth of Binary Tree - Easy - 5 minutes - https://leetcode.com/problems/maximum-depth-of-binary-tree/
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1


    # 543. Diameter of Binary Tree - Easy - 39 min - https://leetcode.com/problems/diameter-of-binary-tree/
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # keep global res 
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            
            res = max(res, left_depth + right_depth)
            return max(left_depth, right_depth) + 1

        dfs(root)

        return res 
           
        
    # 110. Balanced Binary Tree - 1 Hour
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.abs_h = 0
         
        def dfs(root):
            if not root: return [True, 0]
            
            right_d = dfs(root.right)
            left_d = dfs(root.left)
            balanced = (left_d[0] and right_d[0] and abs(left_d[1] - right_d[1]) <= 1)

            return [balanced, max(right_d[1], left_d[1]) + 1]
            
        return dfs(root)[0]


        
 


            


