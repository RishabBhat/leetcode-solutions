"""
Problem: Range Sum of BST
Link: https://leetcode.com/problems/range-sum-of-bst/description/
Difficulty: Easy

Approach:
simple dfs, if we see the current val is higher than the high, we recurse left
because we know that every value to the right is greater since this is a valid bst.
vice versa for any values lower than left.
the recursive case is just adding dfs(left) and dfs(right) to the res, to explore
the entire range. then finally return res

Time Complexity: O(N)
Space Complexity: O(h) where h is the height of the tree (recursive call stack)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root):
            if not root:
                return 0
            elif root.val > high:
                return dfs(root.left)
            elif root.val < low:
                return dfs(root.right)
            else:
                return root.val + dfs(root.left) + dfs(root.right)

        return dfs(root)
