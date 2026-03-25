"""
Problem: Sum root to leaf numbers
Link: https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
Difficulty: medium

Approach:
this is a dfs approach, we konw that we need to traverse to every single leaf node 
in the tree. lets go to each one and ask a simple question: is this the end of the 
root -> leaf path. if so, we can add this to our current value. if not (has children), 
then we can dfs the children as well by adding dfs of left and right to 
get the total value for all nodes. 

Time Complexity: O(n)
Space Complexity: O(h) where h is the height of the tree (log (n) avg, o(n) worst case skewed)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(root, val):
            if not root:
                return 0
            
            val = val * 10 + root.val

            if not root.left and not root.right:
                return val
            return dfs(root.left, val) + dfs(root.right, val)

        return dfs(root, 0)
        
