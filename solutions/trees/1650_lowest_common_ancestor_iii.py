"""
Problem: Lowest Common Ancestor of a Binary Tree III
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
Difficulty: medium

Approach:
- 

Time Complexity: O(h) where h is the height of the tree. In the worst case, both pointers each travel 
the length of both paths, which are at most h nodes long, so it's O(2h) which simplifies to O(h).
Space Complexity: O(1)
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        while a != b:
            a = a.parent if a else q
            b = b.parent if b else p
        return a