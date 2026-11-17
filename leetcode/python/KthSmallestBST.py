# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        counter = 0
        KthSmallest = None
        flag = True
        def recrs(node):
            if node == None:
                return
            nonlocal counter, KthSmallest, flag
            if flag:
                recrs(node.left)
                counter += 1
                if counter == k:
                    KthSmallest = node.val
                    flag = False
                recrs(node.right)
        recrs(root)
        
        return KthSmallest
    
    
"""
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        array = []
        def recrs(node):
            if node == None:
                return
            recrs(node.left)
            array.append(node.val)
            recrs(node.right)
        recrs(root)
        
        return array[k-1]
"""

# alternate solution i came up with
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/