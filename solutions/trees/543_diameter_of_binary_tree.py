"""
Problem: Diameter of a binary tree
Link: https://leetcode.com/problems/diameter-of-binary-tree/
Difficulty: Easy

Approach:

create a non local max value variable that we update with the current max value
as we go through a dfs of the tree. at the end return max

within the dfs, we just return the maximum possible height at each node
up to the parent, and to calculate diamater it adds max height from left
and max height from right.

Time Complexity: O(n)
Space Complexity: O(h) - o(log n) balanced, o(n) worst case skewed
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxVal = 0

        def dfs(root):
            if not root:
                return 0
            l_height = dfs(root.left)
            r_height = dfs(root.right)
            self.maxVal = max(self.maxVal, l_height + r_height)

            return 1 + max(l_height, r_height)
        dfs(root)
        return self.maxVal