# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        array = []
        def recrs(node):
            if node == None:
                return
            array.append(node)
            recrs(node.left)
            recrs(node.right)
        recrs(root)
        for i in range(len(array) - 1):
            array[i].left = None
            array[i].right = array[i+1]
        if array:
            array[-1].left = array[-1].right = None
        

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/