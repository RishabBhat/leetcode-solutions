"""
Problem: Count Nodes Equal to Average of Subtree
Link: https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/
Difficulty: Medium

Approach:
we keep track of the left sum and right sum at each node
and calculate the total sum and total count
then we see if the current node is == average and iterate res
then we just keep traversing up via dfs

Time Complexity: O(n)
Space Complexity: O(h) - o(logn) for balanced tree, o(n) for skewed.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(node): # return (total_sum, total_count)
            if not node:
                return (0, 0)
            
            left_sum, left_count = dfs(node.left)
            right_sum, right_count = dfs(node.right)
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            if node.val == (total_sum // total_count):
                self.res += 1
            
            return (total_sum, total_count)
            
        dfs(root)
        return self.res