# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    depth = 0
    max_depth = 0
    
    def maxDepth(self, root):
        Solution.depth = 0
        Solution.max_depth = 0
        self._maxDepth(root)
        return Solution.max_depth
    
    def _maxDepth(self, root):
        if root == None:
            return
        Solution.depth += 1
        if not root.left and not root.right:
            if Solution.depth > Solution.max_depth:
                Solution.max_depth = Solution.depth
        self._maxDepth(root.left)
        self._maxDepth(root.right)
        Solution.depth -= 1
        
print(Solution().maxDepth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))

# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/