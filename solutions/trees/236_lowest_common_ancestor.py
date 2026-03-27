"""
Problem: Lowest Common Ancestor of a Binary Tree
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
Difficulty: medium

Approach:
we use post order traversal to return up the values if we find 
p and q. if they come from both left and right
then we know the current node is the lca
if not then we just return up whatever came in

Time Complexity: O(log(n))
Space Complexity: O(h) where h is the hight of the tree.
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if not node or node == p or node == q:
                return node
            
            left = dfs(node.left)
            right = dfs(node.right)

            if left and right:
                return node

            return left if left else right
        
        return dfs(root)
