# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sortedArrayToBST(self, nums):
        length = len(nums)
        tree = TreeNode(nums[(length-1)//2])
        
        def recrs(node, l, c, r):
            if l != c:
                left_index = (c+l)//2
                node.left = TreeNode(nums[left_index])
                recrs(node.left, l, left_index, c-1)
                
            if r != c:
                right_index = (r+c+1)//2
                node.right = TreeNode(nums[right_index])
                recrs(node.right, c+1, right_index, r)
        
        recrs(tree, 0, (length-1)//2, length-1)
        return tree


# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
