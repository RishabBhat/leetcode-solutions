"""
Problem: Binary Tree Right Side View
Link: https://leetcode.com/problems/binary-tree-right-side-view/
Difficulty: Medium

Approach:
this is just level order traversal, but we only
save the right most element in each level

Time Complexity: O(n)
Space Complexity: O(n)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        q = deque()
        q.append(root)
        res = []
        while q:
            right = None

            for _ in range(len(q)):
                node = q.popleft()

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                right = node.val
            res.append(right)
        return res

