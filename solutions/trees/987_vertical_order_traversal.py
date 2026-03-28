"""
Problem: Vertical order traversal of a binary tree
Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
Difficulty: hard

Approach:
- create a columns dictionary and append rows and node values per column
- keep track of min and max cols as well
- traverse over the range of min and max cols to create a res array
- and in each one append the value of the node, sort each column
- so that its sorted by rows adn then values to tie break.

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        self.min_col = 0
        self.max_col = 0
        cols = defaultdict(list)

        def dfs(node, row, col):
            if not node:
                return
            self.min_col = min(self.min_col, col)
            self.max_col = max(self.max_col, col)
            cols[col].append([row, node.val])
            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)
        
        
        dfs(root, 0, 0)

        res = []

        for c in range(self.min_col, self.max_col + 1):
            res.append([val for r, val in sorted(cols[c])])
        return res