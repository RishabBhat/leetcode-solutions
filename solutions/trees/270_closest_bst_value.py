"""
Problem: Closest Binary Search Tree Value
Link: https://leetcode.com/problems/closest-binary-search-tree-value/description/
Difficulty: Easy

Approach:

since its a valid bst, we can quickly make our way to the bottom through dfs. we don't 
need recursion, we just need to go left if the val is > target and vice versa

Time Complexity: O(log(n))
Space Complexity: O(h) where h is the height of the tree.
-> o(log(n) average or o(n) worst case (skewed))
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val

        while root:

            if abs(target - root.val) < abs(target - closest):
                closest = root.val
            if abs(target - root.val) == abs(target - closest):
                closest = min(closest, root.val)

            if root.val < target:
                root = root.right
            elif root.val > target:
                root = root.left
            else:
                return root.val
        
        return closest
