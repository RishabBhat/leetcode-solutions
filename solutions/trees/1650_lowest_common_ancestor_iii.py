"""
Problem: [Title]
Link: https://leetcode.com/problems/[slug]/
Difficulty: [Easy/Medium/Hard]

Approach:
- 

Time Complexity: O()
Space Complexity: O()
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # currP = A currQ = A
        currP, currQ = p, q

        while currP != currQ:
            currP = q if not currP else currP.parent
            currQ = p if not currQ else currQ.parent

        return currP