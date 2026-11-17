# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        return self.recrsion(root, 0, targetSum)
        
    
    def recrsion(self, root, curr_sum, targetSum):
        if not root:
            return False
        curr_sum += root.val
        if root.left == None and root.right == None and curr_sum == targetSum:
            return True
        return self.recrsion(root.left, curr_sum, targetSum) or self.recrsion(root.right, curr_sum, targetSum)
        
    
# https://leetcode.com/problems/path-sum/
