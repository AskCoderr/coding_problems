# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def pathSum(self, root, targetSum):
        path_sums = []
        def recrs(node, arr, curr_sum):
            if node == None:
                return
            curr_sum += node.val
            arr.append(node.val)
            
            if node.left == node.right == None:
                if curr_sum == targetSum:
                    path_sums.append(arr)
                    return
                
            recrs(node.left, [i for i in arr], curr_sum)
            recrs(node.right, [j for j in arr], curr_sum)
        
        recrs(root, [], 0)
        return path_sums

# https://leetcode.com/problems/path-sum-ii/description/
